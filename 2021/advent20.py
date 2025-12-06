import timeit
import numpy as np


class FastEnhancer:
    def __init__(self, alg, grid_lines):
        self.alg = np.zeros(512, dtype=int)
        for idx,char in enumerate(alg):
            if char == "#":
                self.alg[idx] = 1
        self.numrows = len(grid_lines)
        self.numcols = len(grid_lines[0])
        self.grid = np.zeros((self.numrows, self.numcols), dtype=int)
        for row, line in enumerate(grid_lines):
            for col, char in enumerate(line):
                if char == '#':
                    self.grid[row, col] = 1
        self.undefined_pixel_state = 0

    def enhance_image(self, fast=False):
        # create temp grid with two additional rows in every direction:
        newrows = np.full((2, self.numcols),
                          self.undefined_pixel_state, dtype=int)
        tempgrid = np.vstack([newrows, self.grid, newrows])
        newcols = np.full((self.numrows + 4, 2),
                          self.undefined_pixel_state, dtype=int)
        tempgrid = np.column_stack([newcols, tempgrid, newcols])
        temprows = self.numrows +4
        tempcols = self.numcols +4

        # create new grid, with one additional rows in every direction:
        self.numrows +=2
        self.numcols +=2
        newgrid = np.zeros((self.numrows, self.numcols), dtype=int)

        if fast != True:
            # process every pixel for new grid
            for col in range(1, tempcols -1):
                for row in range(1, temprows -1):
                    index = tempgrid[row-1,col-1] * 2**8 + tempgrid[row-1,col] * 2**7 + tempgrid[row-1,col+1] * 2**6  + \
                            tempgrid[row,  col-1] * 2**5 + tempgrid[row,  col] * 2**4 + tempgrid[row,  col+1] * 2**3  + \
                            tempgrid[row+1,col-1] * 2**2 + tempgrid[row+1,col] * 2**1 + tempgrid[row+1,col+1] * 2**0 
                    newgrid[row-1,col-1] = self.alg[index]
        else:
            # process every pixel for new grid
            for col in range(1, tempcols -1):
                index = 511 * self.undefined_pixel_state #state outside of grid = 511 or 0 (all lit or all off)
                for row in range(1, temprows -1):
                    # go down one row -> shift value up 3 rows, remove highest row and add new low row
                    index = (index << 3) & 511
                    index += tempgrid[row+1,col-1] * 2**2 + tempgrid[row+1,col] * 2**1 + tempgrid[row+1,col+1] * 2**0

                    #index_comp = tempgrid[row-1,col-1] * 2**8 + tempgrid[row-1,col] * 2**7 + tempgrid[row-1,col+1] * 2**6  + \
                    #        tempgrid[row,  col-1] * 2**5 + tempgrid[row,  col] * 2**4 + tempgrid[row,  col+1] * 2**3  + \
                    #        tempgrid[row+1,col-1] * 2**2 + tempgrid[row+1,col] * 2**1 + tempgrid[row+1,col+1] * 2**0 
                
                    newgrid[row-1,col-1] = self.alg[index]

        # update enhancer with new image
        self.grid = newgrid
        if self.alg[0] == 1 and self.alg[-1] == 0:
            self.undefined_pixel_state ^= 1

    def get_lit_pixels(self):
        return np.sum(self.grid)

class Enhancer:
    def __init__(self, alg, grid_lines):
        self.alg = alg
        self.grid = {(row, col): val for row, line in enumerate(
            grid_lines) for col, val in enumerate(line)}
        self.minrow = min([coord[0] for coord in self.grid.keys()])
        self.maxrow = max([coord[0] for coord in self.grid.keys()])
        self.mincol = min([coord[1] for coord in self.grid.keys()])
        self.maxcol = max([coord[1] for coord in self.grid.keys()])
        self.undefined_pixel_state = "."

    def get_3by3(self, coord):
        row = coord[0]
        col = coord[1]
        return [(r, c)for r in [row-1, row, row+1] for c in [col-1, col, col+1]]

    def get_binary_str(self, coord):
        str = ""
        for pos in self.get_3by3(coord):
            if self.grid.get(pos, self.undefined_pixel_state) == ".":
                str += "0"
            else:
                str += "1"
        return str

    def get_index(self, coord):
        return int(self.get_binary_str(coord), 2)

    def get_processed_pixel(self, coord):
        return self.alg[self.get_index(coord)]

    def print_grid(self):
        for row in range(self.minrow, self.maxrow+1):
            print("")
            for col in range(self.mincol, self.maxcol+1):
                print(self.grid.get((row, col), "."), end="")
        print("")

    def enhance_image(self):
        new_grid = {}
        self.minrow -= 1
        self.maxrow += 1
        self.mincol -= 1
        self.maxcol += 1
        for row in range(self.minrow, self.maxrow+1):
            for col in range(self.mincol, self.maxcol+1):
                new_grid[(row, col)] = self.get_processed_pixel((row, col))
        self.grid = new_grid
        if self.alg[0] == '#' and self.alg[-1] == '.':
            if self.undefined_pixel_state == '#':
                self.undefined_pixel_state = '.'
            elif self.undefined_pixel_state == '.':
                self.undefined_pixel_state = '#'

    def get_lit_pixels(self):
        return list(self.grid.values()).count("#")


def p1(lines):
    alg = lines[0]
    lines = lines[2:]
    enhancer = Enhancer(alg, lines)
    fastenhancer = FastEnhancer(alg, lines)
    fastenhancer.enhance_image()
    fastenhancer.enhance_image()
    for i in range(2):
        enhancer.enhance_image()
    #print(f"\nNumber of lit pixels: {enhancer.get_lit_pixels()}")
    return enhancer.get_lit_pixels()


def p2(lines):
    alg = lines[0]
    lines = lines[2:]
    enhancer = Enhancer(alg, lines)
    for i in range(50):
        enhancer.enhance_image()
        #print(f"After {i+1} iterations: {enhancer.get_lit_pixels()} are lit.")
    return enhancer.get_lit_pixels()

def p2_fast(lines):
    alg = lines[0]
    lines = lines[2:]
    enhancer = FastEnhancer(alg, lines)
    for i in range(50):
        enhancer.enhance_image()
        #print(f"After {i+1} iterations: {enhancer.get_lit_pixels()} are lit.")
    return enhancer.get_lit_pixels()

def p2_faster(lines):
    alg = lines[0]
    lines = lines[2:]
    enhancer = FastEnhancer(alg, lines)
    for i in range(50):
        enhancer.enhance_image(fast=True)
        #print(f"After {i+1} iterations: {enhancer.get_lit_pixels()} are lit.")
    return enhancer.get_lit_pixels()

f = open("input20.txt", "r")
lines = [line.strip() for line in f]


start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2 (fast): {p2_fast(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2 (faster): {p2_faster(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)