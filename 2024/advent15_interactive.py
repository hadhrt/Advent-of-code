import timeit
from enum import Enum
from pynput import keyboard
from pynput.keyboard import Key

DIR = {
        "^": complex(-1, 0),
        "v": complex( 1, 0),
        ">": complex( 0, 1),
        "<": complex( 0,-1)}

class P2_Grid ():
    DIR = {
        "^": complex(-1, 0),
        "v": complex( 1, 0),
        ">": complex( 0, 1),
        "<": complex( 0,-1)}
    def __init__(self, lines):
        self.grid = {}
        self.robot_pos = None
        input_split = lines.index("")
        grid_lines,move_lines= lines[:input_split], lines[input_split+1:]
        self.moves = "".join(move_lines)
        self.grid_size = (len(grid_lines), 2*len(grid_lines[0]))
        for row, line in enumerate(grid_lines):
            for col, val in enumerate(line):
                if val == "#": 
                    self.grid[complex(row,2*col  )] = "#"
                    self.grid[complex(row,2*col+1)] = "#"
                elif val == "O": 
                    self.grid[complex(row,2*col  )] = "["
                    self.grid[complex(row,2*col+1)] = "]"
                elif val == ".": 
                    self.grid[complex(row,2*col  )] = "."
                    self.grid[complex(row,2*col+1)] = "."
                elif val == "@": 
                    self.grid[complex(row,2*col  )] = "@"
                    self.grid[complex(row,2*col+1)] = "."
                    self.robot_pos = complex(row,2*col)
                else:
                    assert(False)
    
    
    def move_item(self, item_pos, move, checkonly = False):
        if item_pos == None:
            item_pos = self.robot_pos
        assert(self.grid.get(item_pos) != None)
        if self.grid.get(item_pos) == "#":
            return False
        if self.grid.get(item_pos) == ".":
            return True
        if move in "<>" or self.grid.get(item_pos) == "@":
            if self.grid.get(item_pos) in "@[]":
                next_pos = item_pos + DIR[move]
                assert(self.grid.get(item_pos) != None)
                if self.move_item(next_pos, move):
                    self.grid[next_pos] = self.grid[item_pos]
                    self.grid[item_pos] = "."
                    if item_pos == self.robot_pos: self.robot_pos = next_pos
                    return True
                else:
                    return False
            assert(False)
        elif move in "^v":
            if self.grid.get(item_pos) == "[":
                item_pos_l,item_pos_r = item_pos, item_pos + complex(0,1)
            elif self.grid.get(item_pos) == "]": 
                item_pos_l,item_pos_r = item_pos + complex(0,-1), item_pos
            else:
                assert(False)
            next_pos_l = item_pos_l + DIR[move]
            next_pos_r = item_pos_r + DIR[move]
            assert(self.grid.get(next_pos_l) != None)
            assert(self.grid.get(next_pos_r) != None)
            if self.move_item(next_pos_l, move, True) and self.move_item(next_pos_r, move, True):
                if not checkonly:
                    self.move_item(next_pos_l, move)
                    self.move_item(next_pos_r, move)
                    self.grid[next_pos_l] = self.grid[item_pos_l]
                    self.grid[item_pos_l] = "."
                    if item_pos_l == self.robot_pos: self.robot_pos = next_pos_l
                    self.grid[next_pos_r] = self.grid[item_pos_r]
                    self.grid[item_pos_r] = "."
                    if item_pos_r == self.robot_pos: self.robot_pos = next_pos_r
                return True
            else:
                return False

        else:
            assert(False)


    def __str__(self):
        grid_str = ""
        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                grid_str += self.grid.get(complex(row,col))
            grid_str += "\n"
        return grid_str
    
    def get_GPS(self):
        return int(sum([pos.real*100+pos.imag for pos,item in self.grid.items() if item =="["]))




f = open("input15.txt", "r")
lines = [line.strip() for line in f]
my_grid = P2_Grid(lines)
print(my_grid)

def on_key_release(key):
    if key == Key.right:
        my_grid.move_item(move=">", item_pos= None)
        print(my_grid)
    elif key == Key.left:
        my_grid.move_item(move="<", item_pos= None)
        print(my_grid)
    elif key == Key.up:
        my_grid.move_item(move="^", item_pos= None)
        print(my_grid)
    elif key == Key.down:
        my_grid.move_item(move="v", item_pos= None)
        print(my_grid)
    elif key == Key.esc:
        exit()

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

