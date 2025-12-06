import timeit
import math

def p1(lines):
    values = 0
    l1 = map(int,lines[0].split(":")[1].split())
    l2 = map(int,lines[1].split(":")[1].split())
    races = list(zip(l1,l2))
    options = []
    for time_allowed,record_distance in races:
        possible_options = []
        for hold_down_time in range(1,time_allowed):
            time_remaining = time_allowed - hold_down_time
            distance = time_remaining*hold_down_time
            if distance > record_distance:
                possible_options.append((hold_down_time, distance))
        options.append(tuple(possible_options))
    values = 1
    for possible_options in options:
        values *= len(possible_options)
    return values


def p2(lines):
    values = 0
    time_allowed = int(lines[0].split(":")[1].replace(" ",""))
    record_distance = int(lines[1].split(":")[1].replace(" ",""))

    # d = (t_max - t_hold) * t_hold
    # d = t_max*t_hold -t_hold^2
    # t_hold^2 -t_max*t_hold +d = 0
    # t_hold = t_max/2 +- sqrt((t_max/2)^2-d)

    min_hold_time = math.ceil((time_allowed/2) - math.sqrt(math.pow((time_allowed/2),2) - record_distance))
    max_hold_time = math.floor((time_allowed/2) + math.sqrt(math.pow((time_allowed/2),2) - record_distance))
    return max_hold_time-min_hold_time + 1
    

f = open("input6.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')


start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')