

def p1(lines):
    values = 0
    sensors = []
    beacons = []
    for line in lines:
        #Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        line = line[9:].replace(": closest beacon is at",",")
        line = line.split(",")
        Sx,Sy,Bx,By = [int(l[3:]) for l in line]
        sensor_range = abs(Bx-Sx)+abs(By-Sy)
        sensors.append(((Sx,Sy), sensor_range))
        beacons.append((Bx,By))
        
    y = 2000000

    
    x_ranges = sorted([get_covered_xrange(sensor, y) for sensor in sensors if get_covered_xrange(sensor, y)])
    x_min = min([x[0] for x in x_ranges])
    x_max = max([x[1] for x in x_ranges])
    for x in range(x_min,x_max+1):
        if (x,y) in beacons:
            continue
        for x_range in x_ranges:
            if x >= x_range[0] and x <= x_range[1]:
                values +=1
                break

    
    #print(sensors)
    #print (x_ranges) 
    
    return values

def get_covered_xrange(sensor, y):
    point,sensor_range = sensor
    sx,sy = point
    range_for_x = sensor_range - abs(sy-y)
    if range_for_x >0:
        return (sx - range_for_x, sx + range_for_x)
    return None
    

def p2(lines):
    values = 0
    sensors = []
    beacons = []
    for line in lines:
        #Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        line = line[9:].replace(": closest beacon is at",",")
        line = line.split(",")
        Sx,Sy,Bx,By = [int(l[3:]) for l in line]
        sensor_range = abs(Bx-Sx)+abs(By-Sy)
        sensors.append(((Sx,Sy), sensor_range))
        beacons.append((Bx,By))
   
    
    max_x = 4000000
    max_y = 4000000
    
    

    found_pos = []

    for y in range(0,max_y+1):
        if y%(max_y//10) == 0: print(f"{((y*10)//(max_y//10))}%")
        x_ranges = sorted([get_covered_xrange(sensor, y) for sensor in sensors if get_covered_xrange(sensor, y)])
        x = 0
        for x_range in x_ranges:
            #print((x,x_range))
            while x < x_range[0]:
                #print(f"found: {(x,y)}")
                found_pos.append((x,y))
                x+=1
            if x_range[1]+1 > x:
                x = x_range[1]+1
    
    sensor_pos = [x[0] for x in sensors]
    found_pos = [x for x in found_pos if x not in sensor_pos]
    found_pos = [x for x in found_pos if x not in beacons]
    return found_pos[0][0]*4000000+found_pos[0][1]
    return found_pos
    
    
f = open("input15.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )