import timeit


class Grid():
    def __init__(self, lines):
        self.grid = {}
        self.size = (len(lines))
        for row,line in enumerate(lines):
            for col,val in enumerate(line):
                self.grid[complex(row,col)] = val

    def __repr__(self) -> str:
        ret = ""
        for row in range(self.size):
            for col in range(self.size):
                ret += self.grid.get(complex(row,col))
            ret += "\n"
        return ret[:-1]
    
    def p1_find_xmas(self) -> int:
        xmas_found = 0
        # find all X values:
        X_value_coords = [coord for (coord, value) in self.grid.items() if value == "X"]
        for coord in X_value_coords:
            xmas_found +=self.p1_check_for_MASes(coord)
        return xmas_found

    def p1_check_for_MASes(self, coord):
        found = 0
        dirs = ((complex( 1, 0), complex( 2, 0), complex ( 3, 0)),
                (complex(-1, 0), complex(-2, 0), complex (-3, 0)),
                (complex( 0, 1), complex( 0, 2), complex ( 0, 3)),
                (complex( 0,-1), complex( 0,-2), complex ( 0,-3)),
                (complex( 1, 1), complex( 2, 2), complex ( 3, 3)),
                (complex(-1,-1), complex(-2,-2), complex (-3,-3)),
                (complex(-1, 1), complex(-2, 2), complex (-3, 3)),
                (complex( 1,-1), complex( 2,-2), complex ( 3,-3)))
        for dir in dirs:
            test = [self.grid.get(coord+offset) for offset in dir]
            if test == ["M","A","S"]: 
                found +=1
                #print(f"({int(coord.real)},{int(coord.imag)})")
        return found
                
    def p2_find_xmas(self) -> int:
        xmas_found = 0
        # find all X values:
        A_value_coords = [coord for (coord, value) in self.grid.items() if value == "A"]
        for coord in A_value_coords:
            xmas_found +=self.p2_check_for_X_MAS(coord)
        return xmas_found

    def p2_check_for_X_MAS(self, coord):
        found = 0
        offsets =  (complex( -1, -1), complex( -1, 1), 
                    complex ( 1, -1), complex( 1, 1))
        valid_values = (["M","M",
                         "S","S"],
                        ["S","M",
                         "S","M"],
                        ["S","S",
                         "M","M"],
                        ["M","S",
                         "M","S"])
        value = [self.grid.get(coord+offset) for offset in offsets]
        if value in valid_values: 
            found +=1
        return found
    

def p1(lines):
    values = 0
    my_grid = Grid(lines)
    #print(my_grid)
    return my_grid.p1_find_xmas()


def p2(lines):
    values = 0
    my_grid = Grid(lines)
    #print(my_grid)
    return my_grid.p2_find_xmas()
    

f = open("input4.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')