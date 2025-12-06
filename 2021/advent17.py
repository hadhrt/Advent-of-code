import timeit
import re

OVERSHOTX = -1
OVERSHOTY = -2


def p1(lines):
    values = 0
    for line in lines:
        #target area: x=20..30, y=-10..-5
        target_area_str = re.findall(r"(-?\d+)",line)
        target_area = tuple(map(int,target_area_str))
    best_velocity = (0,0)
    valid_velocities = set()
    for x in range(1, target_area[1]+1):
        for y in range(target_area[2],1000):
            values +=1
            ret = int(launch_probe(complex(x,y), target_area))
            #print(f"{x},{y} -> {ret}")
            if ret > best_velocity[1]:
                best_velocity = (complex(x,y),ret)
            if ret >= 0:
                valid_velocities.add((x,y))
            if ret == OVERSHOTX:
                break
    print(f"Part 1: {best_velocity[1]}")
    print(f"Part 2: {len(valid_velocities)}")
    print(f"{values} iterations")
    return best_velocity


def p2(lines):
    values = 0
    for line in lines:
        pass
    return values
    
def launch_probe(velocity, target_area):
    pos = complex(0,0)
    y_max = 0
    while True:
        pos += velocity
        if pos.imag > y_max:
            y_max = pos.imag

        if velocity.real > 0: velocity -=  1 # apply drag
        velocity -= complex(0,1)

        if pos.real > target_area[1]: # overshot x
            return OVERSHOTX
        if pos.imag < target_area[2]: # overshot y
            return OVERSHOTY
        if pos.real >= target_area[0] and pos.imag <= target_area[3]: #in target_area
            return y_max

f = open("input17.txt", "r")
lines = [line.strip() for line in f]
  

start = timeit.default_timer()
p1(lines)
#print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

#start = timeit.default_timer()
#print (f"Part 2: {p2(lines)}")
#stop = timeit.default_timer()
#print('Time: ', stop - start)