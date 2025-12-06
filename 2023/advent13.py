import timeit

def p1(lines):
    values = 0
    for line in lines:
        pass
    return values


def p2(lines):
    values = 0
    for line in lines:
        pass
    return values
    

f = open("input.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')