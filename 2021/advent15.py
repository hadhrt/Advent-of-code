import timeit
from collections import defaultdict
import heapq


def dijkstra_naive(lines):
    values = 0
    grid = {}
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            grid[(row, col)] = int(val)
    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1
    start = (0, 0)
    end = (max_row, max_col)

    # Dijkstra:
    # init
    unvisited_nodes = set(grid.keys())
    min_distances = defaultdict(lambda: float("inf"))
    min_distances[start] = 0
    # main algo
    while unvisited_nodes:
        # print(f"{len(unvisited_nodes)} Nodes left in Queue")
        # get min_node
        current_node = None
        for node in unvisited_nodes:
            if current_node == None:
                current_node = node
            else:
                if min_distances[node] < min_distances[current_node]:
                    current_node = node
        if current_node == end:
            return min_distances[end]
        unvisited_nodes.remove(current_node)
        # update neighbours
        for adj in get_adj(current_node, grid):
            if adj in unvisited_nodes:
                alternative_dist = min_distances[current_node] + grid[adj]
                if alternative_dist < min_distances[adj]:
                    min_distances[adj] = alternative_dist
    return -1


def dijkstra_priority_queue(lines):
    values = 0
    grid = {}
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            grid[(row, col)] = int(val)
    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1
    start = (0, 0)
    end = (max_row, max_col)

    # Dijkstra with prio queue:
    # init
    min_distances = defaultdict(lambda: float("inf"))
    min_distances[start] = 0
    prioqueue = []
    heapq.heappush(prioqueue, (0, start))
    num_nodes_visited = 0
    # main algo
    while prioqueue:
        # get min_node
        current_distance, current_node = heapq.heappop(prioqueue)
        # skip node if it has been processed already
        if current_distance > min_distances[current_node]:
            continue
        if current_node == end:
            print(f"Nodes visited by Dijkstra: {num_nodes_visited}")
            return min_distances[end]
        # update neighbours
        num_nodes_visited += 1
        for adj in get_adj(current_node, grid):
            alternative_dist = min_distances[current_node] + grid[adj]
            if alternative_dist < min_distances[adj]:
                min_distances[adj] = alternative_dist
                heapq.heappush(prioqueue, (alternative_dist, adj))

    return -1


def astar(lines):
    values = 0
    grid = {}
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            grid[(row, col)] = int(val)
    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1
    start = (0, 0)
    end = (max_row, max_col)

    # Dijkstra with prio queue:
    # init
    visited = set()
    min_distances = defaultdict(lambda: float("inf"))
    min_distances[start] = 0
    prioqueue = []
    heapq.heappush(prioqueue, (0, start))
    num_nodes_visited = 0
    # main algo
    while prioqueue:
        # get min_node
        current_distance, current_node = heapq.heappop(prioqueue)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == end:
            print(f"Nodes visited by A*: {num_nodes_visited}")
            return min_distances[end]
        # update neighbours
        num_nodes_visited += 1
        for adj in get_adj(current_node, grid):
            projected_dist = min_distances[current_node] + grid[adj] + (abs(adj[0]-end[0]) + abs(adj[1]+end[1])) 
            distance_to_node = min_distances[current_node] + grid[adj]
            if distance_to_node < min_distances[adj]:
                min_distances[adj] = distance_to_node
                heapq.heappush(prioqueue, (projected_dist, adj))

    return -1


def get_adj(coord, grid):
    adj = {(coord[0] + off_row,  coord[1] + off_col)
           for off_row, off_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]}
    return {coord for coord in adj if coord in grid}


def create_p2_map(lines):
    num_rows = len(lines)
    num_cols = len(lines[0])
    linelist = [['X'] * (num_cols *5) for i in range(num_rows*5)] 
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            for x in range(5):
                for y in range(5):
                    new_row = x * num_rows + row
                    new_col = y * num_cols + col
                    linelist[new_row][new_col] = str((int(val) + x + y - 1) % 9 + 1)
    return ["".join(line) for line in linelist]



f = open("input15.txt", "r")
lines = [line.strip() for line in f]

'''
start = timeit.default_timer()
print(f"Part 1 (dijkstra_naive): {dijkstra_naive(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
'''

start = timeit.default_timer()
print(f"Part 1 (dijkstra_priority_queue): {dijkstra_priority_queue(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 1 (A*): {astar(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

lines2 = create_p2_map(lines)


start = timeit.default_timer()
print(f"Part 2 (dijkstra_priority_queue): {dijkstra_priority_queue(lines2)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2 (A*): {astar(lines2)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
