import timeit
from enum import Enum
from pynput import keyboard
from pynput.keyboard import Key

DIR = {
    "^": complex(-1, 0),
    "v": complex( 1, 0),
    ">": complex( 0, 1),
    "<": complex( 0,-1)}


def p1(lines):

    grid = {}
    robot_pos = None
    input_split = lines.index("")
    grid_lines,move_lines= lines[:input_split], lines[input_split+1:]
    moves = "".join(move_lines)
    grid_size = (len(grid_lines), len(grid_lines[0]))
    for row, line in enumerate(grid_lines):
        for col, val in enumerate(line):
            if val == "@":
                robot_pos = complex(row,col)

            grid[complex(row,col)] = val
    
    #print("Initial state:")
    #print_grid(grid, grid_size)

    for move in moves:
        #input()
        #print(f"Move {move}:")
        if try_to_move(grid, robot_pos, move):
            robot_pos += DIR[move]
        #print_grid(grid,grid_size)

    #print("Final state:")
    #print_grid(grid, grid_size)

    return int(sum([pos.real*100+pos.imag for pos,item in grid.items() if item =="O"]))

def print_grid(grid, grid_size):
    grid_str = ""
    for row in range(grid_size[0]):
        for col in range(grid_size[1]):
            grid_str += grid.get(complex(row,col))
        grid_str += "\n"
    print(grid_str)

def try_to_move(grid, item_pos, move):
    assert(grid.get(item_pos) != None)
    if grid.get(item_pos) == "#":
        return False
    if grid.get(item_pos) == ".":
        return True
    if grid.get(item_pos) == "O" or grid.get(item_pos) == "@":
        next_pos = item_pos + DIR[move]
        assert(grid.get(item_pos) != None)
        if try_to_move(grid, next_pos, move):
            grid[next_pos] = grid[item_pos]
            grid[item_pos] = "."
            return True
        else:
            return False
    assert(False)



def p2(lines):

    grid = {}
    robot_pos = None
    input_split = lines.index("")
    grid_lines,move_lines= lines[:input_split], lines[input_split+1:]
    moves = "".join(move_lines)
    grid_size = (len(grid_lines), 2*len(grid_lines[0]))
    for row, line in enumerate(grid_lines):
        for col, val in enumerate(line):
            if val == "#": 
                grid[complex(row,2*col  )] = "#"
                grid[complex(row,2*col+1)] = "#"
            elif val == "O": 
                grid[complex(row,2*col  )] = "["
                grid[complex(row,2*col+1)] = "]"
            elif val == ".": 
                grid[complex(row,2*col  )] = "."
                grid[complex(row,2*col+1)] = "."
            elif val == "@": 
                grid[complex(row,2*col  )] = "@"
                grid[complex(row,2*col+1)] = "."
                robot_pos = complex(row,2*col)
            else:
                assert(False)

    
    print("Initial state:")
    print_grid(grid, grid_size)
    i = 0 

    for move in moves:
        #input()
        #print(f"Move {move}:")
        if try_to_move_p2(grid, robot_pos, move):
            robot_pos += DIR[move]
        #print_grid(grid,grid_size)

    print("Final state:")
    print_grid(grid, grid_size)

    return int(sum([pos.real*100+pos.imag for pos,item in grid.items() if item =="["]))

    
def try_to_move_p2(grid, item_pos, move, checkonly = False):
    assert(grid.get(item_pos) != None)
    if grid.get(item_pos) == "#":
        return False
    if grid.get(item_pos) == ".":
        return True
    if move in "<>" or grid.get(item_pos) == "@":
        if grid.get(item_pos) in "@[]":
            next_pos = item_pos + DIR[move]
            assert(grid.get(item_pos) != None)
            if try_to_move_p2(grid, next_pos, move):
                grid[next_pos] = grid[item_pos]
                grid[item_pos] = "."
                return True
            else:
                return False
        assert(False)
    elif move in "^v":
        if grid.get(item_pos) == "[":
            item_pos_l,item_pos_r = item_pos, item_pos + complex(0,1)
        elif grid.get(item_pos) == "]": 
            item_pos_l,item_pos_r = item_pos + complex(0,-1), item_pos
        else:
            assert(False)
        next_pos_l = item_pos_l + DIR[move]
        next_pos_r = item_pos_r + DIR[move]
        assert(grid.get(next_pos_l) != None)
        assert(grid.get(next_pos_r) != None)
        if try_to_move_p2(grid, next_pos_l, move, True) and try_to_move_p2(grid, next_pos_r, move, True):
            if not checkonly:
                try_to_move_p2(grid, next_pos_l, move)
                try_to_move_p2(grid, next_pos_r, move)
                grid[next_pos_l] = grid[item_pos_l]
                grid[item_pos_l] = "."
                grid[next_pos_r] = grid[item_pos_r]
                grid[item_pos_r] = "."
            return True
        else:
            return False

    else:
        assert(False)


f = open("input15.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')



def on_key_release(key):
    if key == Key.right:
        print("Right key clicked")
    elif key == Key.left:
        print("Left key clicked")
    elif key == Key.up:
        print("Up key clicked")
    elif key == Key.down:
        print("Down key clicked")
    elif key == Key.esc:
        exit()
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

