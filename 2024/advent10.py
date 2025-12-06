import timeit

def p1(lines):
    grid = {}
    
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == ".":
                grid[complex(row,col)] = 99
            else:
                grid[complex(row,col)] = int(val)
    
    trailheads = [(coord,val) for coord,val in grid.items() if val == 0]

    adj = (complex(-1, 0), complex( 1, 0),
           complex( 0,-1), complex( 0, 1))
    trails_found = []

    for trailhead in trailheads:
        node_queue = set([trailhead])
        visited_nodes = set()
        trail_ends =  set()

        while node_queue:
            current_node = node_queue.pop()
            assert(current_node not in visited_nodes)
            if current_node[1] == 9:
                trail_ends.add(current_node)
                continue
            for offset in adj:
                next_node = (current_node[0] + offset, grid.get(current_node[0] + offset))
                if next_node != None and next_node not in visited_nodes:
                    if next_node[1] == current_node[1]+1:
                        node_queue.add(next_node)
        
        trails_found.append((trailhead[0],len(trail_ends)))
    return sum([trails for _,trails in trails_found])




ADJ = (complex(-1, 0), complex( 1, 0),
           complex( 0,-1), complex( 0, 1))

def p2(lines):
    grid = {}
    
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == ".":
                grid[complex(row,col)] = 99
            else:
                grid[complex(row,col)] = int(val)
    
    trailheads = [(coord,val) for coord,val in grid.items() if val == 0]

    trail_map = {}

    for trailhead in trailheads:
        get_trails(trailhead, trail_map, grid)


    return sum([trail_map.get(trailhead) for trailhead in trailheads])
    
def get_trails(current_node, trail_map, grid):
    if current_node in trail_map:
        return trail_map[current_node]
    if current_node[1] == 9:
        return 1

    num_of_trails = 0
    for offset in ADJ:
        next_node = (current_node[0] + offset, grid.get(current_node[0] + offset))
        # ist nicht im grid
        if next_node[1] == None:
            continue
        # ist nicht erreichbar
        if next_node[1] != current_node[1]+1:
            continue
        num_of_trails += get_trails(next_node, trail_map, grid)
    
    assert(current_node not in trail_map)
    trail_map[current_node] = num_of_trails
    
    return num_of_trails


f = open("input10.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')