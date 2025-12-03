import timeit


def p1(lines):
    value = 0

    grid = {complex(row,col) : int(val) for row,line in enumerate(lines) for col,val in enumerate(line)}
    for line in lines:
        pass
        
    return value


def p2(lines):
    value = 0

    for line in lines:
        pass
        
    return value
 

f = open(r"2025/python/Inputs/example.input", "r")
#f = open(r"2025/python/Inputs/01.input", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')