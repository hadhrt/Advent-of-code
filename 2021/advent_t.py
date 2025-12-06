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
print('Time: ', stop - start)

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)