from collections import deque

class State:
    def __init__(self, cave, fallen_rocks, height):
        self.cave = cave
        self.statestr = ""
        self.fallen_rocks = fallen_rocks
        self.height = height

        for row in range(cave.lastrow,cave.lastrow-10,-1):
            row_s = ""
            for col in range(7):
                row_s += cave.grid.get(complex(row,col), "X")
            self.statestr += f"|{row_s}|\n"
            
    def __str__(self):
        return (f"{self.fallen_rocks} Rocks have fallen, Tower height: {self.height}\n{self.statestr}") 
        
    def __eq__(self, other):
        if isinstance(other,State): return self.statestr == other.statestr
        return False
        
    

    
class Shape:
    
    shape_types =[    
    ([ 0+2j, 0+3j, 0+4j, 0+5j ],1),
    ([ 0+3j, 1+2j, 1+3j, 1+4j, 2+3j ],3),
    ([ 0+2j, 0+3j, 0+4j, 1+4j, 2+4j ],3),
    ([ 0+2j, 1+2j, 2+2j, 3+2j ],4),
    ([ 0+2j, 0+3j, 1+2j, 1+3j ],2)]

    def __init__(self, type, row):
        self.rocks = {rock_coord+row+1:"@" for rock_coord in Shape.shape_types[type][0]}
        self.height = Shape.shape_types[type][1]

    def move_to(self, new_coords):
        self.rocks = {rock_coord:"@" for rock_coord in new_coords}

class Cave:
    def __init__(self):
        self.lastrow = 0
        self.lastshape = -1
        # self.lastshape = 0

        # init grid
        self.grid = {}
        self.lastrow = 0
        for i in range(7):
            coord = complex(self.lastrow, i)
            self.grid[coord] = "-"
        
        
    def __str__(self):
        s = ""
        for row in range(self.lastrow,self.lastrow-20,-1):
            row_s = ""
            #if row <0: continue
            for col in range(7):
                row_s += self.grid.get(complex(row,col), "X")
            s += f"|{row_s}|\n"
        return s


    def process_jet_pattern(self,jet_pattern):
        part_1_done = False
        part_2_done = False
        fallen_rocks = 0
        height_list = [0]
        pattern_idx = len(jet_pattern)-1
        period_start_idx = 0
        period_state = None
        print_progress = True
        shape = self.add_next_shape()
        #if print_progress: print("Rock begins falling:")
        #if print_progress: self.draw_falling_shape(shape)   
                
        while not (part_1_done and part_2_done):
            pattern_idx = (pattern_idx+1) % len(jet_pattern)
            jet = jet_pattern[pattern_idx]
            
            if jet == "<":
                self.move_shape_left(shape)
            if jet == ">":
                self.move_shape_right(shape)

            if not self.move_shape_down(shape):
                self.settle_shape(shape)
                fallen_rocks +=1
                height_list.append(self.lastrow)
                if not part_1_done:
                    if fallen_rocks == 2022:
                        print (f"Part 1: {self.lastrow}")
                        part_1_done = True
                    
                if not part_2_done:
                    if fallen_rocks == 1735 + 1732:
                        print(State(self, fallen_rocks, self.lastrow))
                    # um den Sonderfall beim start des Feldes zu umgehen
                    if fallen_rocks >= 1732:
                        # immer wenn erste Shape fertig gefallen ist
                        if self.lastshape == 0:
                            # das erste mal startet wird der perioden index festgelegt und state gespeichert
                            if period_start_idx == 0:
                                period_start_idx = pattern_idx
                                period_state = State(self, fallen_rocks, self.lastrow)
                                print(f"Period State defined: {period_state} period_start_idx: {period_start_idx}")
       
                            #Shape 1 ist gefallen und es ist wieder der gleiche gust pattern index
                            elif pattern_idx == period_start_idx:
                                print(f"Pattern Index: {pattern_idx}")
                                second_state = State(self, fallen_rocks, self.lastrow)
                                if second_state == period_state:
                                    print(f"Second State found: {second_state}")
                                    period_length = second_state.fallen_rocks - period_state.fallen_rocks
                                    period_height_increase = second_state.height - period_state.height
                                    print(f"Period length: {period_length} with height increase: {period_height_increase}")
                                    rock_falling_goal = 1000000000000
                                    periods = rock_falling_goal//period_length
                                    rocks_before_period = rock_falling_goal % periods                                
                                    print(f"Periods: {periods} starting with: {rocks_before_period}")
                                    total_rocks = rocks_before_period + (periods * period_length)
                                    total_height = height_list[rocks_before_period] + (periods * period_height_increase)
                                    print(f"Total Rocks:: {total_rocks} total height: {total_height}")
                                    part_2_done = True
                        
                #if pattern_idx == len(jet_pattern)-1:
                #    state = State(self, fallen_rocks, self.lastrow)
                #    print(state)

                shape = self.add_next_shape()

          

    def draw_falling_shape(self,shape):
        s = ""
        printed = False
        for row in range(self.lastrow,self.lastrow-20,-1):
            row_s = ""
            for col in range(7):
                coord = complex(row,col)
                if shape.rocks.get(coord): 
                   row_s += "@"
                else:
                    row_s += self.grid.get(coord, "X")
            if row_s == "......." and not printed:
                pass
            else:
                s += f"|{row_s}|\n"
                printed = True
        print(s)

    def add_next_shape(self):
        self.add_rows_to_grid(3)
        shape = self.get_next_shape()
        self.add_rows_to_grid(shape.height)
        return shape

    def move_shape_right(self,shape):
        new_coords =  [(coord+1j) for coord in shape.rocks.keys()]
        for coord in new_coords:
            if self.grid.get(coord,"X")  != ".":
                return False
        shape.move_to(new_coords)
        return True
        
    def move_shape_left(self,shape):
        new_coords =  [(coord-1j) for coord in shape.rocks.keys()]
        for coord in new_coords:
            if self.grid.get(coord,"X")  != ".":
                return False
        shape.move_to(new_coords)
        return True
        
    def move_shape_down(self,shape):
        new_coords =  [(coord-1) for coord in shape.rocks.keys()]
        for coord in new_coords:
            if self.grid.get(coord,"X")  != ".":
                return False
        shape.move_to(new_coords)
        return True

    def add_rows_to_grid(self,rows):
        for row in range(self.lastrow+1,self.lastrow+rows+1):
            for col in range(7):
                coord = complex(row, col)
                self.grid[coord] = "."
        self.lastrow += rows

    def get_next_shape(self):
        self.lastshape = (self.lastshape +1)%5
        return Shape(self.lastshape, self.lastrow)   
    
    def collide(self,shape):
        for rock_coord in shape.rocks.keys():
            if grid.get(rock_coord,"X") != ".":
                return True
        return False
        
    def settle_shape(self,shape):
        for rock_coord in shape.rocks.keys():
            self.grid[rock_coord] = "#"
        self.update_last_row()
        shape = None
        
    def update_last_row(self):
        #print(f"Last row: {self.lastrow}")
        for row in range(self.lastrow, (self.lastrow -3 -4 -1) , -1):
            for col in range(7):
                coord = complex(row, col)
                if self.grid.get(coord,"X")  == "X":
                    print(f"ERROR UPDATE LAST ROW: COORD OUT OF GRID: {coord}")
                if self.grid.get(coord) != ".":
                    self.lastrow = row
                    return
        print("ERROR UPDATE LAST ROW: ROW NOT FOUND")   
    

    
def p1(line):

    cave = Cave()
    return cave.process_jet_pattern(line)

    

f = open("input17.txt", "r")
line = [line.strip() for line in f][0]
p1(line)


