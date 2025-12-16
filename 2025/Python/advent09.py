import timeit
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def p1(lines):
    tiles = [tuple(map(int, line.split(","))) for line in lines]
    max_rect = 0
    for i, tile_1 in enumerate(tiles):
        for j, tile_2 in enumerate(tiles):
            if i < j:
                rect = (abs(tile_1[0] - tile_2[0]) + 1) * (
                    abs(tile_1[1] - tile_2[1]) + 1
                )
                max_rect = rect if rect > max_rect else max_rect
    print_example_tiles(tiles)
    return max_rect


def print_example_tiles(tiles):
    if len(tiles) == 8:
        s = "\n"
        for y in range(7 + 2):
            for x in range(11 + 3):
                if (x, y) in tiles:
                    s += "#"
                else:
                    s += "."
            s += "\n"
        print(s)


def draw_tiles(tiles, rect):
    fig, ax = plt.subplots()
    x_vals = [x[0] for x in tiles]
    y_vals = [x[1] for x in tiles]
    ax.plot(x_vals, y_vals, "ro-", ms=0.1)
    ax.plot([x_vals[0], x_vals[-1]], [y_vals[0], y_vals[-1]], "ro-", ms=0.1)
    rect = patches.Rectangle(
        (rect[0], rect[1]),
        rect[2],
        rect[3],
        linewidth=1,
        edgecolor="b",
        facecolor="none",
    )
    ax.add_patch(rect)
    plt.show()


def smallify(tiles):
    pass
    return


def p2(f_lines):
    tiles = [tuple(map(int, line.split(","))) for line in f_lines]
    draw_rect = [0, 0, 0, 0]

    # calc all circumfence lines
    vert_lines = []  # ((from_x, to_x), y)
    horz_lines = []  # (x, (from_y, to_y))
    for i in range(len(tiles)):
        if i == len(tiles) - 1:
            curr = tiles[i]
            next = tiles[0]
        else:
            curr = tiles[i]
            next = tiles[i + 1]
        if curr[0] == next[0]:
            vert_lines.append(
                (
                    curr[0], 
                    (min(curr[1], next[1]), max(curr[1], next[1]))
                    )
                )
        elif curr[1] == next[1]:
            horz_lines.append(
                (
                    (min(curr[0], next[0]), max(curr[0], next[0])),
                    curr[1]
                    )
                )

    # calc all rectangles
    max_rect = 0
    for i, tile_1 in enumerate(tiles):
        for j, tile_2 in enumerate(tiles):
            if i < j:
                rect = (abs(tile_1[0] - tile_2[0]) + 1) * (
                    abs(tile_1[1] - tile_2[1]) + 1
                )
                # if rect is too small no need to continue
                if rect <= max_rect:
                    continue
                # does any line cross the rect?
                is_valid = True
                x_min = min(tile_1[0], tile_2[0])
                x_max = max(tile_1[0], tile_2[0])
                y_min = min(tile_1[1], tile_2[1])
                y_max = max(tile_1[1], tile_2[1])

                for vert_line in vert_lines:
                    # is x-coord inside rect?
                    if vert_line[0] < x_max and vert_line[0] > x_min:
                        # is the line completely outside of the rect?
                        if vert_line[1][0] < y_min and vert_line[1][1] < y_min:
                            continue
                        if vert_line[1][0] > y_max and vert_line[1][1] > y_max:
                            continue
                        is_valid = False
                        break
                    
                if is_valid:
                    for horz_line in horz_lines:
                        # is y-coord inside rect ?
                        if horz_line[1] < y_max and horz_line[1] > y_min:
                            # is the line completely outside of the rect?
                            if horz_line[0][0] < x_min and horz_line[0][1] < x_min:
                                continue
                            if horz_line[0][0] > x_max and horz_line[0][1] > x_max:
                                continue
                                # line intersects!
                            is_valid = False
                            break
                # does rect open to the outside?

                if is_valid:
                    draw_rect = [x_min, y_min, x_max - x_min, y_max - y_min]
                    max_rect = rect
    #draw_tiles(tiles, draw_rect)
    return max_rect


#  f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/09.input", "r")
lines = [line.strip("\n") for line in f]
f.close()

start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")
