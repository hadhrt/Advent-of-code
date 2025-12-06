import timeit

ADJ_OFFSET = (-1 - 1j, -1 + 0j, -1 + 1j, 0 - 1j, 0 + 1j, 1 - 1j, 1 + 0j, 1 + 1j)


def print_grid(grid):
    print_string = ""
    for coord, val in grid.items():
        if coord.imag == 0:
            print_string += "\n"
        print_string += val
    print(print_string)


def p1(lines):
    accessible_rolls = 0
    grid = {
        complex(row, col): val
        for row, line in enumerate(lines)
        for col, val in enumerate(line)
    }

    for coord, val in grid.items():
        adjecent_rolls = [grid.get(coord + offset) for offset in ADJ_OFFSET].count("@")
        accessible_rolls += adjecent_rolls < 4 and val == "@"
        pass

    return accessible_rolls


def p2(lines):
    grid = {
        complex(row, col): val
        for row, line in enumerate(lines)
        for col, val in enumerate(line)
    }
    removed_rolls = 0

    while True:
        updated_grid = {}
        for coord, val in grid.items():
            adjecent_rolls = [grid.get(coord + offset) for offset in ADJ_OFFSET].count(
                "@"
            )
            if adjecent_rolls < 4 and val == "@":
                updated_grid[coord] = "."
                removed_rolls += 1
            else:
                updated_grid[coord] = grid[coord]
            pass
        if updated_grid == grid:
            break
        grid = updated_grid
        # print_grid(grid)

    return removed_rolls


# f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/04.input", "r")
lines = [line.strip() for line in f]

start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")
