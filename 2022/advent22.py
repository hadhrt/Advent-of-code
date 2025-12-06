import timeit
import curses
import itertools
from collections import deque

FILE = "input22.txt"
FACING = ">v<^"
ANIMATE = True
MOVE = False
ROWS = 50
COLS = 50

class Board2:
    grids = []
    stdscr = None
    num_rows = ROWS
    num_cols = COLS
    
    player_pos = (0,0)
    player_grid = None
    player_dir = ">"
    get_right={">":"v", "v":"<", "<":"^", "^":">"}
    get_left={">":"^", "^":"<", "<":"v", "v":">"}
    move_offsets={">":(0,1), "<":(0,-1), "^":(-1,0), "v":(1,0)}
    grid_row_offset =[0,0,50,100,100,150]
    grid_col_offset =[50,100,50,0,50,0]
    grid_trans = {(0,">"):(1, ">"), (1,">"):(4, "<"), (2,">"):(1, "^"), (3,">"):(4, ">"), (4,">"):(1, "<"), (5,">"):(4, "^"),
                  (0,"<"):(3, ">"), (1,"<"):(0, "<"), (2,"<"):(3, "v"), (3,"<"):(0, ">"), (4,"<"):(3, "<"), (5,"<"):(0, "v"),
                  (0,"^"):(5, ">"), (1,"^"):(5, "^"), (2,"^"):(0, "^"), (3,"^"):(2, ">"), (4,"^"):(2, "^"), (5,"^"):(3, "^"),
                  (0,"v"):(2, "v"), (1,"v"):(2, "<"), (2,"v"):(4, "v"), (3,"v"):(5, "v"), (4,"v"):(5, "<"), (5,"v"):(1, "v")}  


        
    def __init__(self, stdscr, lines):
        self.stdscr = stdscr
        lines = [line.replace("\n","") for line in lines]
        lines = lines[:-2]
        
        #create 50*50 lines
        gridlines = []
        gridlines.append([line[50:100] for row,line in enumerate(lines) if row <50])
        gridlines.append([line[100:150] for row,line in enumerate(lines) if row <50])
        gridlines.append([line[50:100] for row,line in enumerate(lines) if row >=50 and row <100])
        gridlines.append([line[0:50] for row,line in enumerate(lines) if row >=100 and row <150])
        gridlines.append([line[50:100] for row,line in enumerate(lines) if row >=100 and row <150])
        gridlines.append([line[0:50] for row,line in enumerate(lines) if row >=150 and row <200])
        
        #create the six grids from lines
        for gridline in gridlines: 
            #print(gridline)        
            self.grids.append({(row,col):val for row,line in enumerate(gridline) for col,val in enumerate(line)})    
        self.player_grid = self.grids[0]
        

    def print_player_grid(self):
        self.print_grid(self.player_grid)
        
    def print_grid(self, grid):
        height, width = self.stdscr.getmaxyx()
        #print grid
        for pos,v in grid.items():
            if pos[0]<height and pos[1]< width-1:
                self.stdscr.addstr(*pos,v,curses.color_pair(0))
        if self.player_pos[0]<height and self.player_pos[1]< width and grid == self.player_grid:
            self.stdscr.addstr(*self.player_pos,self.player_dir,curses.color_pair(1))
        if height > 51:
            self.stdscr.addstr(51,10,"Player Grid: "+str(self.grids.index(self.player_grid)),curses.color_pair(1))
        self.stdscr.refresh()
        return
    
    def rotate_player(self, dir):
        match dir:
            case "R":
                self.player_dir = self.get_right[self.player_dir]
            case "L":
                self.player_dir = self.get_left[self.player_dir]
            case _:
                assert(False) 
                
    def move_player(self, steps):
        for i in range(steps):
            if self.move_player_one_step() == False:
                return False  
                
    def move_player_one_step(self):
        off = self.move_offsets[self.player_dir]
        new_pos = (self.player_pos[0] + off[0], self.player_pos[1] + off[1])
        match self.player_grid.get(new_pos,"oob"):
            case ".":
                self.player_pos = new_pos
                return True
            case "#":
                return False
            case "oob":
                return self.move_player_to_new_grid()
            case _:
                assert(False)  
                
    def move_player_to_new_grid(self):
        new_state = self.grid_trans[(self.grids.index(self.player_grid),self.player_dir)]
        new_player_grid = player_grid = self.grids[new_state[0]]
        inc_dir = new_state[1]
        #get outgoing position:
        match self.player_dir:
            case ">":
                side_pos = self.player_pos[0]
            case "<":
                side_pos = 49-self.player_pos[0]        
            case "^":
                side_pos = self.player_pos[1]  
            case "v":
                side_pos = 49-self.player_pos[1]
            case _:
                print(self.player_dir)
                assert(False)
        # get incoming position to new grid
        match inc_dir:
            case ">":
                new_player_pos = (side_pos,0)
            case "<":
                new_player_pos = (49-side_pos,49)        
            case "^":
                new_player_pos = (49,side_pos)  
            case "v":
                new_player_pos = (0,49-side_pos) 
            case _:
                assert(False)
        # if player would hit a wall, dont execute grid change
        if player_grid.get(new_player_pos) == "#":
            return False
        # move player to new grid
        self.player_grid = new_player_grid
        self.player_pos = new_player_pos
        self.player_dir = inc_dir
        
    def get_result(self):
        row_offset = self.grid_row_offset[self.grids.index(self.player_grid)]
        col_offset = self.grid_col_offset[self.grids.index(self.player_grid)]
        return(self.player_pos[0]+1+row_offset)*1000 + (self.player_pos[1]+1+col_offset)*4 + FACING.index(self.player_dir)   
    
    
class Board:
    grid = None
    stdscr = None
    num_cols = None
    num_rows = None
    player_pos = None
    player_dir = ">"
    get_right={">":"v", "v":"<", "<":"^", "^":">"}
    get_left={">":"^", "^":"<", "<":"v", "v":">"}
    player_path={}
    
    def __init__(self, stdscr, lines):
        lines = [line.replace("\n","") for line in lines]
        lines = lines[:-2]
        self.num_rows = len(lines)
        self.num_cols = max([len(line) for line in lines])
        lines = [line.ljust(self.num_cols) for line in lines]
        grid = {(row,col):val for row,line in enumerate(lines) for col,val in enumerate(line)}
        self.grid =  grid
        self.stdscr = stdscr
        self.init_player()

    
    def print_grid(self):
        height, width = self.stdscr.getmaxyx()
        #print grid
        for pos,v in self.grid.items():
            if pos[0]<height and pos[1]< width-1:
                self.stdscr.addstr(*pos,v,curses.color_pair(0))
        #print player
        if self.player_pos[0]<height and self.player_pos[1]< width:
            self.stdscr.addstr(*self.player_pos,self.player_dir,curses.color_pair(1))
        self.stdscr.refresh()
        return
        
    def init_player(self):
        for col in range(self.num_cols):
            if self.grid.get((0,col),"~") == ".":
                self.player_pos = (0,col)
                return
        assert(False)
       
    def move_player(self, steps):
        for i in range(steps):
            if self.move_player_one_step() == False:
                return False
            if ANIMATE:
                self.print_grid()
                curses.napms(8)
     
    def rotate_player(self, dir):
        match dir:
            case "R":
                self.player_dir = self.get_right[self.player_dir]
                if ANIMATE:
                    self.print_grid()
                    curses.napms(20)
            case "L":
                self.player_dir = self.get_left[self.player_dir]
                if ANIMATE:
                    self.print_grid()
                    curses.napms(20)
            case _:
                assert(False)

    def move_player_one_step(self):
        match self.player_dir:
            case ">":
                off = (0,1)
                pos_iter = itertools.product([self.player_pos[0]],range(self.num_cols))
            case "<":
                off = (0,-1)
                pos_iter = itertools.product([self.player_pos[0]],reversed(range(self.num_cols)))
            case "^":
                off = (-1,0)
                pos_iter = itertools.product(reversed(range(self.num_rows)),[self.player_pos[1]])
            case "v":
                off = (1,0)
                pos_iter = itertools.product(range(self.num_rows),[self.player_pos[1]])
            case _:
                assert(False)    
        new_pos = (self.player_pos[0] + off[0], self.player_pos[1] + off[1])
        match self.grid.get(new_pos,"oob"):
            case ".":
                self.player_pos = new_pos
                return True
            case "#":
                return False
            case " " | "oob":
                for row,col in pos_iter:
                    new_pos = (row,col)
                    match self.grid.get(new_pos,"oob"):
                        case ".":
                            self.player_pos = new_pos
                            return True 
                        case "#":
                            return False
                        case " ":
                            continue
                        case _:
                            assert(False)
            case _:
                assert(False)
                
    def get_result(self):
       return(self.player_pos[0]+1)*1000 + (self.player_pos[1]+1)*4 + FACING.index(self.player_dir)
        
    
def main(stdscr):

    curses.curs_set(0) # make cursor invisible
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    
    
    f = open(FILE, "r")
    lines = [line for line in f]
    directions = lines[-1]


    my_board = Board(stdscr, lines)
    my_board2 = Board2(stdscr, lines)
    dir_list = deque(directions.replace("R",";R;").replace("L",";L;").split(";"))
    
    while (dir_list):
        move = int(dir_list.popleft())
        my_board.move_player(move)
        my_board2.move_player(move)
        if not dir_list : break
        rota = dir_list.popleft()
        my_board.rotate_player(rota)
        my_board2.rotate_player(rota)

    

    
    if ANIMATE:
        stdscr.getkey()
    
   
    
    
    if MOVE:
        my_board2.print_player_grid()
        k = None
        while (k != ord('q')):
            match k:
                case curses.KEY_RIGHT:
                    my_board2.rotate_player("R")
                    my_board2.print_player_grid()
                case curses.KEY_LEFT:
                    my_board2.rotate_player("L")
                    my_board2.print_player_grid()
                case curses.KEY_UP:
                    my_board2.move_player(1)
                    my_board2.print_player_grid()
        
            # Wait for next input
            k = stdscr.getch()
        


    print("Part 1: " + str(my_board.get_result()))
    print("Part 2: " + str(my_board2.get_result()))
    
    return 


   
curses.wrapper(main)
