import timeit


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


def smallify(tiles):
    pass
    return


def p2(f_lines):
    tiles = [tuple(map(int, line.split(","))) for line in f_lines]
    
    #calc all circumfence lines
    vert_lines = []
    horz_lines = []
    for i in range(len(tiles)):
        if i == len(tiles)-1:
            curr = tiles[i]
            next = tiles[0] 
        else:
            curr = tiles[i]
            next = tiles[i+1]
        if curr[0] == next[0]:
            vert_lines.append((curr[0], (curr[1],next[1])))
        elif curr[1] == next[1]:
            horz_lines.append(((curr[0],next[0]), curr[1]))
    
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
                
                if rect == 30:
                    pass
                
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
                            if horz_line[0][0] < x_min and horz_line[0][0] < x_min:
                                continue
                            if horz_line[0][0] > x_max and horz_line[0][1] > x_max:
                                continue
                                    # line intersects!
                            is_valid = False
                            break    
                if is_valid:
                    max_rect = rect 
    return max_rect



# f = open(r"2025/Inputs/example.input", "r")
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
