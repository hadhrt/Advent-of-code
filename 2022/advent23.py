import curses
from collections import deque

FILE = "input23.txt"



class Board:

    stdscr = None
    elves = None
    steps = 0
    dirs = deque(['N', 'S', 'W', 'E'])
    dir_offs = {'N': ((-1,-1),(-1, 0),(-1, 1)),
                'S': (( 1,-1),( 1, 0),( 1, 1)),
                'W': ((-1,-1),( 0,-1),( 1,-1)),
                'E': ((-1, 1),( 0, 1),( 1, 1))}
    adj_offs = [(-1,-1),(-1, 0),(-1, 1),
                ( 0,-1),        ( 0, 1),
                ( 1,-1),( 1, 0),( 1, 1)]
    
    
    def __init__(self, stdscr, lines):
      
        elves = {(row,col): None for row,line in enumerate(lines) for col,val in enumerate(line) if val == "#"}
        self.elves =  elves
        self.stdscr = stdscr

    def print_grid(self, prop_pos=None, new_elves=None):
        # get size of screeen
        height, width = self.stdscr.getmaxyx()
 
        # get size of elf grid
        off_row = -min(row for row,col in self.elves.keys()) +1
        off_col = -min(col for row,col in self.elves.keys()) +1
        max_row = off_row + max(row for row,col in self.elves.keys()) +2
        max_col = off_col + max(col for row,col in self.elves.keys()) +2
        
        max_screen_row = min(max_row, height)
        max_screen_col = min(max_col, width-1)

        # print grid
        for row in range(max_screen_row):
            for col in range(max_screen_col):
                self.stdscr.addstr(row, col, ".", curses.color_pair(0))
            #self.stdscr.addstr(row, 0, "."*(max_screen_col), curses.color_pair(0))
        
        for pos,val in self.elves.items():
            if pos[0]+off_row < max_screen_row and pos[1]+off_col < max_screen_col:
                if val != None:
                    self.stdscr.addstr(pos[0]+off_row, pos[1]+off_col, '#', curses.color_pair(3))
                else:
                    self.stdscr.addstr(pos[0]+off_row, pos[1]+off_col, '#', curses.color_pair(0))
        if prop_pos != None:
            #draw proposed positions
            '''
            for pos,val in prop_pos.items():
                if pos[0]+off_row < max_screen_row and pos[1]+off_col < max_screen_col:
                    if val > 1:
                        self.stdscr.addstr(pos[0]+off_row, pos[1]+off_col, str(val), curses.color_pair(1))
                    else:
                        self.stdscr.addstr(pos[0]+off_row, pos[1]+off_col, str(val), curses.color_pair(2))
            
            self.stdscr.refresh()
            delay = 500 if self.steps <5 else 50
            curses.napms(delay)
            '''
            
            #self.stdscr.getkey()            
            #clear old elves
            for pos in self.elves.keys():
                if pos[0]+off_row < max_screen_row and pos[1]+off_col < max_screen_col:
                    self.stdscr.addstr(pos[0]+off_row, pos[1]+off_col, '.', curses.color_pair(0))
            #clear invalid proposed pos
            for pos,val in prop_pos.items():
                if pos[0]+off_row < max_screen_row and pos[1]+off_col < max_screen_col:
                    if val > 1:
                        self.stdscr.addstr(pos[0]+off_row, pos[1]+off_col, '.', curses.color_pair(0))    
            #draw new elves            
            for pos in new_elves.keys():
                if pos[0]+off_row < max_screen_row and pos[1]+off_col < max_screen_col:           
                    self.stdscr.addstr(pos[0]+off_row, pos[1]+off_col, '#', curses.color_pair(0))
        
        self.stdscr.refresh()
        delay = 500 if self.steps <5 else 50
        curses.napms(delay)
        #self.stdscr.getkey()
        return
        
    def step_elves(self):
        self.steps += 1
        proposed_poses = {}
        # each elf looks for valid moves
        for elf in self.elves.keys():
            # are no elves adj?
            has_adj = False
            for offset in self.adj_offs:
                if (elf[0]+offset[0], elf[1]+offset[1]) in self.elves:
                    has_adj = True
                    break #offset
            if not has_adj:
                continue #next elf
            # is there a valid direction to go?
            for dir in self.dirs:
                dir_is_valid = True
                # is current direction valid?
                for offset in self.dir_offs[dir]:
                    if (elf[0]+offset[0], elf[1]+offset[1]) in self.elves:
                        dir_is_valid = False
                        break #offset
                        
                if dir_is_valid:
                    prop_pos = (elf[0]+self.dir_offs[dir][1][0], elf[1]+self.dir_offs[dir][1][1])
                    self.elves[elf] = prop_pos 
                    # increase the number of elves at proposed pos  
                    proposed_poses[prop_pos] = proposed_poses.get(prop_pos,0)+1
                    break #dir
        #check if no elf moved
        nobody_moved = all(v is None for v in self.elves.values())
        # move elves:
        new_elves = {}
        for old_pos,new_pos in self.elves.items():
            # move is only 1 elf intends to go there
            if proposed_poses.get(new_pos,0) == 1:
                new_elves[new_pos] = None
            else:
                new_elves[old_pos] = None
                
        #if nobody_moved:
            #self.print_grid(proposed_poses, new_elves)        
        self.print_grid(proposed_poses, new_elves)        
            
        self.elves = new_elves
        self.dirs.append(self.dirs.popleft())
        
        if nobody_moved:
            return self.steps
        else:
            return None
    
    def get_empty_tiles(self):
        min_row = min(row for row,col in self.elves.keys())
        min_col = min(col for row,col in self.elves.keys())
        max_row = max(row for row,col in self.elves.keys())+1
        max_col = max(col for row,col in self.elves.keys())+1
        return (max_row-min_row)*(max_col-min_col) - len(self.elves)
            
def main(stdscr):

    curses.curs_set(0) # make cursor invisible
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    f = open(FILE, "r")
    lines = [line.strip() for line in f]
    myboard = Board(stdscr, lines)
    myboard.print_grid()
    for i in range(10000):
        steps = myboard.step_elves()
        if steps != None:
            break
    print(f"Part 1: {myboard.get_empty_tiles()}")
    print(f"Part 2: {steps}")
    
curses.wrapper(main)
