import timeit
from heapq import heappush, heappop
from dataclasses import dataclass
from functools import total_ordering
from math import inf

DIR = {
        complex(-1, 0):"^",
        complex( 1, 0):"v",
        complex( 0, 1):">",
        complex( 0,-1):"<"}

@dataclass(eq=True, frozen=True)
class Node:
    pos: complex
    direction: complex

    def __lt__(self,other):
        return False


def p1_p2(lines):
    
    start = timeit.default_timer()

    # read grid
    start_dir = complex( 0, 1)
    grid = {}
    for row,line in enumerate(lines):
        for col, val in enumerate(line):
            grid[complex(row,col)] = val
            if val == "S":
                start_pos = complex(row,col)
            if val == "E":
                end_pos = complex(row,col)

    # find shortest paths from "S" to "E"
    parents = {}
    lowest_weight = {}
    node_queue = []
    starting_node = Node(start_pos,start_dir)
    heappush(node_queue, (0,starting_node))
    parents[starting_node] = set()
    end_weight = inf
    endings = set()

    while node_queue:
        current_weight,current_node = heappop(node_queue)
        if current_weight > end_weight:
            continue
        if current_node.pos == end_pos:
            end_weight = current_weight
            endings.add(current_node)
       
        nodes_to_check = ((current_weight + 1000, Node(current_node.pos, current_node.direction * complex(0,1))), # clockwise
                         (current_weight + 1000, Node(current_node.pos, current_node.direction * complex(0,-1))), # counter clockwise
                         (current_weight + 1, Node(current_node.pos+current_node.direction, current_node.direction))) # forward

       
        for new_weight,new_node in nodes_to_check:
            if grid.get(new_node.pos) == "#":
                continue
            if new_node not in lowest_weight:
                lowest_weight[new_node] = new_weight
                parents[new_node] = set([current_node])
                heappush(node_queue, (new_weight,new_node))
            else:
                if new_weight == lowest_weight[new_node]:
                    parents[new_node].add(current_node)

            
    return_queue = endings
    visited = set()
    
    while return_queue:
        current_node = return_queue.pop()
        if current_node not in visited:
            visited.add(current_node)
        else:
            continue
        if current_node != None:
            grid[current_node.pos]="O"
            return_queue.update( parents[current_node])

    grid_str = ""
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            grid_str += grid[complex(row,col)]
        grid_str += "\n"
    
    #print(grid_str)
    

    print(f"Part 1: {end_weight}")

    print(f"Part 2: {len([pos for pos,val in grid.items() if val =="O"])}")

    stop = timeit.default_timer()
    print(f'Time: {(stop - start):.4}')


    return 



f = open("input16.txt", "r")
lines = [line.strip() for line in f]
p1_p2(lines)
