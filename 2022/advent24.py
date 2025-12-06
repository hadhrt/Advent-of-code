import curses
from collections import deque
import timeit
FILE = "input24.txt"



class Board:

    stdscr = None
    blizzards = None
    walls = set()
    player_poses = {(0,1)}
    grid = set()
    steps = 0
    num_rows = 0
    num_cols = 0
    target_pos = None
    goals_reached = 0
    
    

    
    
    def __init__(self, stdscr, lines):
        dirs = {'>', '<', '^', 'v'}
        self.blizzards = [((row,col), val) for row,line in enumerate(lines) for col,val in enumerate(line) if val in dirs]
        self.stdscr = stdscr
        self.num_rows = len(lines)
        self.num_cols = len(lines[0])
        # define walls
        for col in range(self.num_cols):
            self.walls.add((0,col))
            self.walls.add((self.num_rows-1,col))
        for row in range(self.num_rows):
            self.walls.add((row,0))
            self.walls.add((row,self.num_cols-1))       
        self.walls.remove((0,1))
        self.walls.remove((self.num_rows-1, self.num_cols -2))
        self.grid = {(row,col) for row in range(self.num_rows) for col in range(self.num_cols)}
        self.target_pos = (self.num_rows-1, self.num_cols -2)

    def fill_grid(self):
    
        grid = {}
        blizz_count_map = {'>':'2', '<':'2', '^':'2', 'v':'2' , '2':'3', '3':'4' }
        
        # add open spaces
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                grid[(row, col)] = '.'
                        
        # add border:
        for pos in self.walls:
            grid[pos] = '#'        

        # add blizzards
        for pos,dir in self.blizzards:
            if grid[pos] == '.':
                grid[pos] = dir
            else:
                grid[pos] = blizz_count_map[dir]
            
        # add player
        for pos in self.player_poses:
            assert(grid[pos] == 'X' or grid[pos] == '.')
            grid[pos] = 'X'
            
        return grid
        
    def step(self):
        self.steps += 1
        dir_map = {'>':(0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0)}
        adj_offs = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]
        new_blizzards = []
        blizz_poses = set()
        
        # new blizzard positions
        for pos,dir in self.blizzards:
            off_row,off_col = dir_map[dir]
            new_row = pos[0] + off_row
            new_col = pos[1] + off_col
            if new_row == 0:
                new_row = self.num_rows-2
            if new_row ==  self.num_rows-1:
                new_row = 1
            if new_col == 0:
                new_col = self.num_cols-2
            if new_col ==  self.num_cols-1:
                new_col = 1
            new_blizzards.append(((new_row,new_col),dir))
            blizz_poses.add((new_row,new_col))
        
        # new possible player positions
        new_player_poses = set()
        for old_pos in self.player_poses:
            for off_row, off_col in adj_offs:
                new_pos = (old_pos[0]+off_row, old_pos[1]+off_col)
                if new_pos in self.grid and new_pos not in self.walls and new_pos not in blizz_poses:
                    new_player_poses.add(new_pos)
            
        self.player_poses = new_player_poses
        self.blizzards = new_blizzards
        if self.target_pos in self.player_poses:
            self.goals_reached += 1
            self.player_poses = {self.target_pos}
            
            # exit reached 
            if self.goals_reached %2 == 1:
                self.target_pos = (0, 1)
                
            # start reached
            if self.goals_reached %2 == 0:
                self.target_pos = (self.num_rows-1, self.num_cols -2)               
                
            #self.print_grid()
            #self.stdscr.addstr(self.num_rows+1,0, f"Target {self.goals_reached} reached in {self.steps} steps", curses.color_pair(2))
            #self.stdscr.refresh()
            #self.stdscr.getkey()           
            if self.goals_reached == 1:
                print(f"Part 1: {self.steps} steps")
            if self.goals_reached == 3:
                print(f"Part 2: {self.steps} steps")       
            return self.goals_reached    
        else:
            
            if self.goals_reached %2 == 0:
                self.cull_players_forwards()
            else:
                self.cull_players_backwards()
               
            return self.goals_reached
           
    def cull_players_forwards(self):
        player_poses_copy = self.player_poses.copy()
        max_col = max([col for row,col in self.player_poses])
        for pos in player_poses_copy:
            if pos[1] < max_col - 15:
                self.player_poses.remove(pos)

    def cull_players_backwards(self):
        player_poses_copy = self.player_poses.copy()
        min_col = min([col for row,col in self.player_poses])
        for pos in player_poses_copy:
            if pos[1] > min_col + 15:
                self.player_poses.remove(pos)
                
    def print_grid(self):
        grid = self.fill_grid()
        for pos,val in grid.items():
            if val == 'X':
                self.stdscr.addstr(*pos, val, curses.color_pair(1))
            else:
                self.stdscr.addstr(*pos, val, curses.color_pair(0))
        self.stdscr.refresh()
        #self.stdscr.getkey()
        return
            
def main(stdscr):

    curses.curs_set(0) # make cursor invisible
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    f = open(FILE, "r")
    lines = [line.strip() for line in f]
    myboard = Board(stdscr, lines)
    # myboard.print_grid()
    #stdscr.getkey()
    start = timeit.default_timer()
    for i in range(1000): 
        if myboard.step() == 3:
            break
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    '''
        myboard.print_grid()
        if i < 15:
            curses.napms(300)
        elif i < 30:
            curses.napms(200)
        elif i < 80:
            curses.napms(100)
        else:
            curses.napms(20)
        '''

 

    
curses.wrapper(main)
