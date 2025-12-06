import timeit
import numpy as np
from itertools import product

def p1(lines):
    values = 0
    keys = []
    locks = []
    for i in range(len(lines)//8+1):
        l = [list(a) for a in lines[8*i+1:8*i+6]]
        l = list(map(list, zip(*l)))
        pins = [ll.count("#") for ll in l]

        if lines[8*i] == "#####":
            keys.append(pins)
        else:
            locks.append(pins)

    for key,lock in product(keys,locks):
        if all([k+l <= 5 for k,l in zip(key,lock)]):
            values +=1
    


    return values


def p2(lines):
    values = 0
    for line in lines:
        pass
    return values
    

f = open("input25.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')