import timeit
from enum import Enum
import copy


class Step_return(Enum):
    INSIDE = 0
    OUTSIDE = -1
    LOOP = -2


class GridMover:
    DIR_OFFSET = {"^": complex(-1,0),
                  "v": complex(1,0),
                  ">": complex(0,1),
                  "<": complex(0,-1)}
    DIR_TRANSITION = {"^": ">",
                      ">": "v",
                      "v": "<",
                      "<": "^"}
    def __init__(self, lines):
        self.initial_grid = {}
        self.size = (len(lines))
        self.initial_guard_pos = None
        self.initial_guard_dir = "^"
        self.p1_positions = None

        for row,line in enumerate(lines):
            for col,val in enumerate(line):
                self.initial_grid[complex(row,col)] = val
                if val == self.initial_guard_dir:
                    self.initial_guard_pos = complex(row,col)
                    self.initial_grid[complex(row,col)] = "."

        self.grid = copy.copy(self.initial_grid)
        self.guard_pos = self.initial_guard_pos
        self.guard_dir = self.initial_guard_dir

    def __repr__(self) -> str:
        ret = ""
        for row in range(self.size):
            for col in range(self.size):
                ret += self.grid.get(complex(row,col))
            ret += "\n"
        return ret[:-1]
    
    def step_guard(self) -> int:
        assert(self.guard_pos in self.grid)

        # check if we have entered this spot in the same direction before
        if self.grid[self.guard_pos] == self.guard_dir:
            return Step_return.LOOP

        # overwrite current position if we have not been here before
        if self.grid[self.guard_pos] == ".":
            self.grid[self.guard_pos] = self.guard_dir
        
        # set guard to next valid position
        next_pos = self.guard_pos + GridMover.DIR_OFFSET[self.guard_dir]
        while self.grid.get(next_pos) == "#":
            self.guard_dir = GridMover.DIR_TRANSITION[self.guard_dir]
            next_pos = self.guard_pos + GridMover.DIR_OFFSET[self.guard_dir]
        self.guard_pos = next_pos

        # check next position
        if next_pos not in self.grid:
            return Step_return.OUTSIDE
        else:
            return Step_return.INSIDE

                
    def solve_p1(self) -> int:
        assert(self.guard_pos != None)
        assert(self.guard_dir != None)
        assert(self.grid != None)
        while self.step_guard() != Step_return.OUTSIDE:
            pass
        self.p1_positions = [pos for pos in self.grid.keys() if self.grid.get(pos) in ("<",">","v","^")]
        return len(self.p1_positions)
    
    def load_next_grid(self, obstacle_pos) -> bool:
        # check if pos is valid for obstacle
        if obstacle_pos == self.initial_guard_pos:
            return False
        if self.initial_grid.get(obstacle_pos) != ".":
            return False
        if obstacle_pos not in self.p1_positions:
            return False
        self.grid = copy.copy(self.initial_grid)
        self.grid[obstacle_pos] = "#"
        self.guard_pos = self.initial_guard_pos
        self.guard_dir = self.initial_guard_dir
        return True

    def solve_p2(self) -> int:
        if self.p1_positions == None:
            self.solve_p1()
        loop_positions = []
        outside_posistions = []
        for row in range(self.size):
            print(row)
            for col in range(self.size):
                if self.load_next_grid(complex(row,col)):
                    for i in range(self.size*self.size):
                        assert( i != self.size*self.size-1)
                        step_ret = self.step_guard() 
                        if step_ret == Step_return.OUTSIDE:
                            outside_posistions.append(complex(row,col))
                            break
                        if step_ret == Step_return.LOOP:
                            loop_positions.append(complex(row,col))
                            break
        return len(loop_positions)
                        
    
def p1(lines):
    my_grid_mover = GridMover(lines)
    values = my_grid_mover.solve_p1()
    # print(my_grid_mover)
    return values

def p2(lines):
    my_grid_mover = GridMover(lines)
    values = my_grid_mover.solve_p2()
    return values
    

f = open("input6.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')