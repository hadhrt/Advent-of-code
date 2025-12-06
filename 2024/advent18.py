import timeit
from dataclasses import dataclass
from heapq import heappush,heappop

@dataclass(eq=True)
class Node:
    pos:complex

    def __lt__(self, other):
        return False


def p1(lines):

    grid = {}
    for row in range(GRIDMAX+1):
        for col in range(GRIDMAX+1):
            grid[complex(row,col)] = "."
    for line in lines[:BLOCKS]:
        row,col = map(int,line.split(","))
        grid[complex(col,row)] = "#"
    return find_shortest_path(grid)
    
    
def p2(lines):

    grid = {}
    for row in range(GRIDMAX+1):
        for col in range(GRIDMAX+1):
            grid[complex(row,col)] = "."
    for line in lines[:BLOCKS]:
        row,col = map(int,line.split(","))
        grid[complex(col,row)] = "#"

    if SLOW:
        for idx,line in enumerate(lines[BLOCKS+1:]):
            print(idx+BLOCKS)
            row,col = map(int,line.split(","))
            grid[complex(col,row)] = "#"
            if find_shortest_path(grid) == False:
                return line
    else:
        line_min = BLOCKS+1
        line_max = len(lines)-1
        while line_min != line_max-1:
            mid = (line_min+line_max)//2
            for line in lines[line_min:mid]:
                row,col = map(int,line.split(","))
                grid[complex(col,row)] = "#"
            if find_shortest_path(grid) != False:
                line_min = mid
            else:
                for line in lines[line_min:mid]:
                    row,col = map(int,line.split(","))
                    grid[complex(col,row)] = "." 
                line_max = mid 

    
 

    return lines[line_min]
    

def print_grid(grid):
    grid_str = ""
    for row in range(GRIDMAX+1):
        for col in range(GRIDMAX+1):
            grid_str += grid[complex(row,col)]
        grid_str += "\n"
    print(grid_str)

def find_shortest_path(grid):
    start = Node(complex(0,0))
    end_pos = complex(GRIDMAX,GRIDMAX)
    visited_pos = set()
    node_queue = [(0,start)]
    while node_queue:
        current_weight,current_node = heappop(node_queue)
        if current_node.pos in visited_pos:
            continue
        visited_pos.add(current_node.pos)
        #print(current_weight)
        if current_node.pos == end_pos:
            return current_weight   
        for node_offset in (complex(0,-1),complex(0,1),complex(-1,0),complex(1,0)):
            if current_node.pos + node_offset not in grid:
                continue
            if current_node.pos + node_offset in visited_pos:
                continue
            if grid[current_node.pos + node_offset] != ".":
                continue
            heappush(node_queue,(current_weight+1,Node(current_node.pos + node_offset)))

    return False

file = "input18.txt"

if file == "input.txt":
    GRIDMAX = 6
    BLOCKS = 12
else:
    GRIDMAX = 70
    BLOCKS = 1024
SLOW = False

f = open(file, "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')