import timeit
import math

def p1(lines):
    steps = 0
    instructions = lines[0].strip()
    direction_index = "LR"
    maps = {}
    for line in lines[2:]:
        node_start = line[:3]
        node_left = line[7:10]
        node_right = line[12:15]
        maps[node_start] = (node_left, node_right)
    
    current_node = "AAA"
    while current_node != "ZZZ":
        direction = direction_index.index(instructions[steps%len(instructions)])
        steps +=1
        current_node = maps.get(current_node)[direction]
    return steps




def p2(lines):
    direction_index = "LR"
    instructions = lines[0].strip()
    maps = {}
    for line in lines[2:]:
        node_start = line[:3]
        node_left = line[7:10]
        node_right = line[12:15]
        maps[node_start] = (node_left, node_right)

    starting_nodes = set([node for node in maps.keys() if node[2]=="A"])
    end_nodes = set([node for node in maps.keys() if node[2]=="Z"])
    
    path_lengths = []
    for starting_node in starting_nodes:
        # the assumption here is that every starting node leads to exactly one end node
        steps = 0
        current_node = starting_node
        while True:
            if current_node in end_nodes:
                path_lengths.append(steps)
                break
            direction = direction_index.index(instructions[steps%len(instructions)])
            steps +=1
            current_node = maps.get(current_node)[direction] 

    # the assumption here is that length(start -> end) = length(end->end)
    return math.lcm(*path_lengths)


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