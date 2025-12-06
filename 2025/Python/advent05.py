import timeit

    
def p1(lines):
    num_of_fresh_ids = 0

    fresh_id_ranges = []
    lines_id_ranges, lines_ingredient_ids = lines[:lines.index("")], lines[lines.index("")+1:]
    for line in lines_id_ranges:
        fresh_id_ranges.append(tuple(map(int,line.split("-"))))
    # test all id ranges for every id; very inefficient, but fast enough
    for line in lines_ingredient_ids:
        ingredient_id = int(line)
        is_fresh = False
        for id_range in fresh_id_ranges:
            if ingredient_id in range(id_range[0],id_range[1]+1):
                is_fresh  = True
                break
        num_of_fresh_ids += is_fresh
    return num_of_fresh_ids


def p2(lines):
    num_of_fresh_ids = 0
    lines_id_ranges = lines[:lines.index("")]

    # sort all ranges by first boundary, then merge overlapping ranges
    for line in lines_id_ranges:
        fresh_id_ranges = [tuple(map(int,line.split("-"))) for line in lines_id_ranges]
        fresh_id_ranges.sort()

    current_range = fresh_id_ranges.pop(0)
    while fresh_id_ranges:
        next_range = fresh_id_ranges.pop(0)
        # merge with next range if overlap exists
        if next_range[0] <= current_range[1]:
            current_range = (current_range[0], max(current_range[1],next_range[1]))
        # else count elements in merged (or single) range
        else:
            num_of_fresh_ids += current_range[1]-current_range[0]+1
            current_range = next_range
    # count final range
    num_of_fresh_ids += current_range[1]-current_range[0]+1
     
    return num_of_fresh_ids
 

#f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/05.input", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')