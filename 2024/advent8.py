import timeit
from itertools import combinations

def p1(lines):
    antennas = {}
    grid_pos = set()
    antinodes = set()
    for row,line in enumerate(lines):
        for col,val in enumerate(line):
            grid_pos.add(complex(row,col))
            if val == ".":
                continue    
            if val not in antennas:
                antennas[val] = []
            antennas[val].append(complex(row,col))
    for antenna_id,antenna_list in antennas.items():
        for a1,a2 in combinations(antenna_list,2):
            delta = a2-a1
            if a2+delta in grid_pos:
                antinodes.add(a2+delta)
            if a1-delta  in grid_pos:
                antinodes.add(a1-delta)

    return len(antinodes)


def p2(lines):
    values = 0
    antennas = {}
    grid_pos = set()
    antinodes = set()
    for row,line in enumerate(lines):
        for col,val in enumerate(line):
            grid_pos.add(complex(row,col))
            if val == ".":
                continue    
            if val not in antennas:
                antennas[val] = []
            antennas[val].append(complex(row,col))
    for antenna_id,antenna_list in antennas.items():
        for a1,a2 in combinations(antenna_list,2):
            antinodes.add(a1)
            antinodes.add(a2)                
            delta = a2-a1
            for i in range(len(lines)):
                if a1 + (i* delta) not in grid_pos:
                    break
                else:
                    antinodes.add(a1 + (i* delta))
            for i in range(1,len(lines)):
                if a1 - (i* delta) not in grid_pos:
                    break
                else:
                    antinodes.add(a1 - (i* delta))

    return len(antinodes)
    

f = open("input8.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')