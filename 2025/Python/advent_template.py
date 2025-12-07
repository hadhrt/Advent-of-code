import timeit
from dataclasses import dataclass

@dataclass(frozen=True, order = True)
class Coord:
    row: int
    col: int

    def __add__(self, other):
        return Coord(self.row + other.row, self.col + other.col)


ADJ_ALL_OFFSETS = ( Coord(-1,-1), Coord(-1, 0), Coord(-1, 1),
                    Coord( 0,-1),               Coord(-1, 1),
                    Coord( 1,-1), Coord( 1, 0), Coord( 1, 1))

ADJ_ORTH_OFFSETS = (             Coord(-1, 0),   
                    Coord( 0,-1),               Coord(-1, 1),
                                 Coord( 1, 0))

def print_grid(grid):
    print_string = ""
    for coord, val in grid.items():
        if coord.col == 0:
            print_string += "\n"
        print_string += val
    print(print_string)
    
    
def p1(lines):
    value = 0

    #grid = {Coord(row,col) : val for row,line in enumerate(lines) for col,val in enumerate(line)}
    #print_grid(grid)
    for line in lines:
        pass
        
    return value


def p2(lines):
    value = 0

    for line in lines:
        pass
        
    return value
 

f = open(r"2025/Inputs/example.input", "r")
#f = open(r"2025/Inputs/01.input", "r")
lines = [line.strip("\n") for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')