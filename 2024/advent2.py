import timeit
import itertools


def is_safe(levels):
    diffs = [a-b for a,b in zip(levels,levels[1:])]
    if all([x*diffs[0] >0 for x in diffs]):
        if all([abs(x)<=3 for x in diffs]):
            return True
    return False


def p1(lines):
    values = 0
    for line in lines:
        vals = [int(x) for x in line.split()]
        if is_safe(vals):
            values +=1
    return values

def p2(lines):
    values = 0
    for line in lines:
        vals = [int(x) for x in line.split()]
        for i in range(len(vals)):
            vals_skipped = vals[:i]+ vals[i+1:]
            diffs = [a-b for a,b in zip(vals_skipped,vals_skipped[1:])]
            if all([x*diffs[0] >0 for x in diffs]):
                if all([abs(x)<=3 for x in diffs]):
                    values +=1
                    break
    return values

f = open("input2.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')