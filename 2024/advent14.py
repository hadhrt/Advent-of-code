import timeit
from dataclasses import dataclass


GRID_COLS= 101
GRID_ROWS = 103

@dataclass
class Robot:
    vel:complex


def p1(lines):
    start = timeit.default_timer()
    robots = {}


    for line in lines:

        pos_str,vel_str = line.split(" v=")
        col,row = map(int,pos_str[2:].split(","))
        right_vel,down_vel = map(int,vel_str.split(","))
        if robots.get(complex(col, row)) == None:
            robots[complex(col, row)] = []

        robots[complex(col, row)].append(Robot(complex(right_vel,down_vel)))

    p1_val = None
    for i in range(10000):
        robots = step_robots(robots)

        if i == 100:
            

            p1_val = 1
            p1_val *= sum([len(current_robots) for pos,current_robots in robots.items() if pos.real < GRID_COLS//2 and pos.imag < GRID_ROWS//2 ])
            p1_val *= sum([len(current_robots) for pos,current_robots in robots.items() if pos.real < GRID_COLS//2 and pos.imag > GRID_ROWS//2 ])
            p1_val *= sum([len(current_robots) for pos,current_robots in robots.items() if pos.real > GRID_COLS//2 and pos.imag < GRID_ROWS//2 ])
            p1_val *= sum([len(current_robots) for pos,current_robots in robots.items() if pos.real > GRID_COLS//2 and pos.imag > GRID_ROWS//2 ])
            stop = timeit.default_timer()



        if all(len(current_robots)==1 for current_robots in robots.values()):
        
            print(grid_to_str(robots))
            print (f"Part 1: {p1_val}")
            print(f'Time: {(stop - start):.4}')
            return i+1

    return

def grid_to_str(robots):
    grid_str = ""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            if robots.get(complex(col,row)):
                assert(len(robots.get(complex(col,row)))<=9)
                grid_str += str(len(robots.get(complex(col,row))))
            else:
                grid_str += "."
        grid_str += "\n"
    return grid_str

def step_robots(robots):
    new_robots = {}
    for pos, robots_at_pos in robots.items():
        for robot in robots_at_pos:
            new_pos = pos + robot.vel
            if new_pos.real < 0: new_pos += complex(GRID_COLS,0)
            if new_pos.real >= GRID_COLS: new_pos -= complex(GRID_COLS,0)
            if new_pos.imag < 0: new_pos  += complex(0,GRID_ROWS)
            if new_pos.imag >= GRID_ROWS: new_pos -= complex(0,GRID_ROWS)
            if new_robots.get(new_pos) ==  None: new_robots[new_pos] = []
            new_robots[new_pos].append(robot)
    return new_robots



def p2(lines):
    values = 0
    for line in lines:
        pass
    return values
    

f = open("input14.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 2: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')