import timeit
from itertools import product
from dataclasses import dataclass
from collections import Counter

@dataclass(frozen=True)
class Node:
    pos: complex

    def __lt__(self, other):
        return False

ADJ = (complex(-1,0), complex(1,0),
       complex(0,-1), complex(0,1))
CHEAT_OFFS = set([i+j for i,j in product(ADJ, repeat = 2)])

    
def p1(lines):
    grid_size = len(lines)
    grid = {}
    for row,line in enumerate(lines):
        for col, val in enumerate(line):
            if val == "S":
                start_pos = complex(row,col)
            if val == "E":
                end_pos = complex(row,col)
            grid[complex(row,col)] = val

    path = get_path(grid,start_pos,end_pos)
    cheats = get_twostep_cheats(path,MIN_TIME_SAVED)
    c = Counter([time for _,_,time in cheats])
    return c.total()

def get_twostep_cheats(path,min_time_save):
    cheats = []
    for start_pos, time in path.items():
        for offset in CHEAT_OFFS:
            end_pos = start_pos + offset
            if end_pos in path:
                time_saved = path.get(end_pos) - (time +2)
                if time_saved >= min_time_save:
                    cheats.append((start_pos,end_pos, time_saved ))
    return cheats

def get_cheats(path, max_cheat_time, min_time_save):
    cheats = []
    for start_pos, start_time in path.items():
        for end_pos, end_time in path.items():
            if end_time <= start_time:
                continue
            cheat_steps = int(abs(start_pos.real-end_pos.real) + abs(start_pos.imag-end_pos.imag))
            if cheat_steps > max_cheat_time:
                continue
            time_saved = end_time - (start_time + cheat_steps)
            if time_saved < min_time_save:
                continue
            cheats.append((start_pos,end_pos, time_saved ))

    return cheats

def get_path(grid, start_pos, end_pos):

    path = {start_pos:0}
    current_pos = start_pos
    current_duration = 0
    next_pos = current_pos
    while current_pos != end_pos:
        for offset in ADJ:
            if grid.get(current_pos+offset) == "." or grid.get(current_pos+offset) == "E":
                if current_pos+offset in path:
                    continue
                else:
                    assert(next_pos == current_pos)
                    next_pos = current_pos+offset
                    path[next_pos] = current_duration +1
        current_duration += 1
        current_pos = next_pos
    return path

def p2(lines):
    grid_size = len(lines)
    grid = {}
    for row,line in enumerate(lines):
        for col, val in enumerate(line):
            if val == "S":
                start_pos = complex(row,col)
            if val == "E":
                end_pos = complex(row,col)
            grid[complex(row,col)] = val

    path = get_path(grid,start_pos,end_pos)
    cheats = get_cheats(path,20,MIN_TIME_SAVED)
    c = Counter([time for _,_,time in cheats])
    return c.total()

    
MIN_TIME_SAVED = 100
f = open("input20.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')