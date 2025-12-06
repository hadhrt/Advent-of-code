import timeit


def fold_x(coord_set, val):
    new_set = set()
    for coord in coord_set:
        if coord[0] <= val:
            new_set.add(coord)
        else:
            new_set.add((2*val - coord[0], coord[1]))
    return new_set


def fold_y(coord_set, val):
    new_set = set()
    for coord in coord_set:
        if coord[1] <= val:
            new_set.add(coord)
        else:
            new_set.add((coord[0], 2*val - coord[1]))
    return new_set


def p1(lines):
    instructions = lines[lines.index("")+1:]
    coords = lines[:lines.index("")]
    coord_set = set()
    for coord in coords:
        x, y = coord.split(',')
        coord_set.add((int(x), int(y)))
    # print(f"{len(coord_set)}, {coord_set}")

    for instruction_line in instructions:
        axis, val = instruction_line[11:].split("=")
        if axis == "x":
            coord_set = fold_x(coord_set, int(val))
        else:
            coord_set = fold_y(coord_set, int(val))
        # print(f"{len(coord_set)}, {coord_set}")
        break

    return len(coord_set)


def p2(lines):
    instructions = lines[lines.index("")+1:]
    coords = lines[:lines.index("")]
    coord_set = set()
    for coord in coords:
        x, y = coord.split(',')
        coord_set.add((int(x), int(y)))
    
    for instruction_line in instructions:
        axis, val = instruction_line[11:].split("=")
        if axis == "x":
            coord_set = fold_x(coord_set, int(val))
        else:
            coord_set = fold_y(coord_set, int(val))
        # print(f"{len(coord_set)}, {coord_set}")
        
    print_grid(coord_set)
    return len(coord_set)


def print_grid(coord_set):
    max_x = max(coord_set, key=lambda x: x[0])[0]
    max_y = max(coord_set, key=lambda x: x[1])[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in coord_set:
                print("#", end='')
            else:
                print(".", end='')
        print('')


f = open("input13.txt", "r")
lines = [line.strip() for line in f]


start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
