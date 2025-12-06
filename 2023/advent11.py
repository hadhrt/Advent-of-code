import timeit
import itertools

def p1(lines):
    grid = []
    values = 0
    grid_list = [[val for val in line] for line in lines]
    exp_rows_grid = []
    for row in grid_list:
        if  all([val == "." for val in row]):
            exp_rows_grid.append(row)
        exp_rows_grid.append(row)
    exp_col_grid = [[] for row in exp_rows_grid]


    for col_idx,_ in enumerate(exp_rows_grid[0]):
        # append original value
        for row_idx,_ in enumerate(exp_col_grid):
            exp_col_grid[row_idx].append(exp_rows_grid[row_idx][col_idx])
        # duplicate original value if all values i row are "."
        if all ([row[col_idx] == "." for row in exp_rows_grid]):
            for row_idx,_ in enumerate(exp_col_grid):
                exp_col_grid[row_idx].append(".")

    grid = {(row_idx, col_idx): val for row_idx,row in enumerate(exp_col_grid) for col_idx,val in enumerate(row)}
    galaxies = [pos for pos, val in grid.items() if val == "#"]
    for pos1, pos2 in itertools.combinations(galaxies,2):
        values += abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    return values


def p2(lines, exp_factor = 1000000):
    values = 0
    grid_list = [[val for val in line] for line in lines]
    galaxies = [(row,col) for row, line in enumerate(grid_list) for col, val in enumerate(line) if val == "#"]
    empty_rows = []
    empty_cols = []

    # get all empty rows and cols
    for row_idx,row in enumerate(grid_list):
        if all([val == "." for val in row]):
            empty_rows.append(row_idx)
    for col_idx,_ in enumerate(grid_list[0]):
        if all ([row[col_idx] == "." for row in grid_list]):
            empty_cols.append(col_idx)

    # transform all galaxy coords to include expended space
    updates_galaxies = []
    for row,col in galaxies:
        # how many empty rows before this galaxies row
        emp_row = sum([row > e_row for e_row in empty_rows]) 
        # how many empty cols before this galaxies col
        emp_col = sum([col > e_col for e_col in empty_cols])
        row_offset = emp_row * (exp_factor-1)
        col_offset = emp_col * (exp_factor-1)
        updates_galaxies.append((row + row_offset, col + col_offset))

    for pos1, pos2 in itertools.combinations(updates_galaxies,2):
        values += abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    return values
    



f = open("input11.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
#print (f"Part 1: {p1(lines)}")
print (f"Part 1: {p2(lines,2)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')