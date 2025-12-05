import timeit

ADJ_OFFSETS = (-1-1j, -1+0j, -1+1j,
                0-1j,         0+1j,
                1-1j,  1+0j,  1+1j)

ADJ_OFFSETS_NO_DIAG = (     -1+0j,
                       0-1j,       0+1j,
                             1+0j,)

def print_grid(grid):
    print_string = ""
    for coord, val in grid.items():
        if coord.imag == 0:
            print_string += "\n"
        print_string += val
    print(print_string)   
    
    
def p1(lines):
    value = 0

    # grid = {complex(row,col) : int(val) for row,line in enumerate(lines) for col,val in enumerate(line)}
    # print_grid(grid)
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
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')