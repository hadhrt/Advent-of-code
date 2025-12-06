import timeit
from collections import Counter

def p1(lines):
    left = []
    right = []
    for line in lines:
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    return sum([abs(l-r) for l,r in zip(left,right)])


def p2(lines):
    left = []
    right = []
    for line in lines:
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))
    c = Counter(right)
    return sum([c[val]*val for val in left])
    

f = open("input1.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.3}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.3}')