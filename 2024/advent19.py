import timeit
from functools import cache
from heapq import heappush,heappop

def p1(lines):

    towels = tuple(lines[0].split(", "))
    patterns = lines[2:]
    possible_patterns = 0
    for idx,pattern in enumerate(patterns):
        if create_pattern_prefix(pattern, towels) != 0:
            possible_patterns +=1
    return possible_patterns

@cache
def create_pattern(pattern,towels):
    if len(pattern) == 0:
        return 0
    possible_combinations = 0
    for towel in towels:
        # towel fits at the beginning
        if pattern[:len(towel)] == towel:
            # towel fits complete pattern = 1 possibility
            if len(towel) == len(pattern):
                possible_combinations += 1
                #break
            # towel fits at the end, but there is pattern remaining
            possible_combinations += create_pattern(pattern[len(towel):],towels)
    return possible_combinations  

def p2(lines):
    towels = tuple(lines[0].split(", "))
    patterns = lines[2:]
    possible_patterns = 0
    for idx,pattern in enumerate(patterns):
        #print(idx)
        possible_patterns += create_pattern_prefix(pattern, towels) 
    return possible_patterns

@cache
def create_pattern_prefix(pattern, towels):
    if pattern == "":
        return 1
    posses = 0
    for towel in towels:
        if pattern.startswith(towel):
            posses += create_pattern_prefix(pattern.removeprefix(towel), towels)
    return posses

f = open("input19.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')