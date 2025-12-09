import timeit
import math
import heapq


def p1_and_p2(lines):
    junction_boxes = [tuple(map(int, line.split(","))) for line in lines]
    distance_heap = []
    for i, jb_1 in enumerate(junction_boxes):
        for j, jb_2 in enumerate(junction_boxes):
            # ignore same boxes and duplicate pairings
            if j > i: 
                heapq.heappush(
                    distance_heap,
                    (
                        math.sqrt(
                            pow(jb_1[0] - jb_2[0], 2)
                            + pow(jb_1[1] - jb_2[1], 2)
                            + pow(jb_1[2] - jb_2[2], 2)
                        ),
                        jb_1,
                        jb_2,
                    ),
                )
    circuits = list(set((jb,)) for jb in junction_boxes)
    connections = 0

    while distance_heap:
        _,jb_1,jb_2 = heapq.heappop(distance_heap)
        jb_1_set_index = [i for i,circuit in enumerate(circuits) if jb_1 in circuit][0]
        jb_2_set_index = [i for i,circuit in enumerate(circuits) if jb_2 in circuit][0]
        if jb_1_set_index != jb_2_set_index:
            circuits[jb_1_set_index] = circuits[jb_1_set_index].union(circuits[jb_2_set_index])
            circuits.pop(jb_2_set_index)
        connections += 1
        if connections == 1000:
            p1_val = math.prod(sorted([len(s) for s in circuits])[-3:])
        if len(circuits) == 1:
            p2_val = jb_1[0]*jb_2[0]
            break
    
    return p1_val, p2_val


def p2(lines):
    value = 0

    for line in lines:
        pass

    return value


# f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/08.input", "r")
lines = [line.strip("\n") for line in f]

start = timeit.default_timer()
print(f"Part 1 and 2: {p1_and_p2(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")
