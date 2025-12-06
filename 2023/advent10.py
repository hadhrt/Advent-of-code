import timeit


class Grid():
    NORTH,EAST,SOUTH,WEST = (complex(-1,0), complex(0,1), complex(1,0), complex(0,-1))
    connections = {"|":(NORTH,SOUTH),
                   "-":( EAST, WEST),
                   "L":(NORTH, EAST),
                   "J":(NORTH, WEST),
                   "7":(SOUTH, WEST),
                   "F":(SOUTH, EAST),
                   ".":set(),
                   "S":(NORTH,EAST,SOUTH,WEST)}
    
    def __init__(self, lines):
        self.grid = {}
        self.size = (len(lines))
        for row,line in enumerate(lines):
            for col,val in enumerate(line):
                self.grid[complex(row,col)] = val
                if val == "S": self.start = complex(row,col)
        assert(self.start != None)
        self.path = self.get_path()

    def __repr__(self) -> str:
        ret = ""
        for row in range(self.size):
            for col in range(self.size):
                ret += self.grid.get(complex(row,col))
            ret += "\n"
        return ret[:-1]
    
    def get_connected(self, pos):
        adj_off = self.connections.get(self.grid.get(pos))
        if adj_off == None:
            return []
        return [pos+neighbour for neighbour in adj_off]
    
    def get_starting_connections(self):
        adjs = self.get_connected(self.start)
        ret = []
        for adj in adjs:
            adj_conn = self.get_connected(adj)
            if self.start in adj_conn:
                ret.append(adj)
        return ret

    def get_path(self):
        path = [self.start]
        a = self.get_starting_connections()
        last_node = self.start
        current_node = a[0]
        while True:
            next_node = [node for node in self.get_connected(current_node) if node != last_node][0]
            if next_node == self.start:
                break
            path.append(next_node)
            last_node = current_node
            current_node = next_node
        return path
    
    def print_path(self):
        trans = {"-":"─",
                 "|":"│",
                 "F":"┌",
                 "7":"┐",
                 "L":"└",
                 "J":"┘",
                 ".":" ",
                 "S":"S"}
        ret = ""
        for row in range(self.size):
            for col in range(self.size):
                if complex(row,col) in self.path: 
                    ret += trans.get(self.grid.get(complex(row,col)))
                else:
                    ret += " "
            print(ret)
            ret = ""

    


def p1(lines):
    values = 0
    my_grid = Grid(lines)
    my_grid.print_path()
    return (len(my_grid.get_path())+1)//2
    print(my_grid)
    return values


def p2(lines):
    values = 0
    for line in lines:
        pass
    return values
    

f = open("input.txt", "r")
lines = [line.strip() for line in f]

  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')