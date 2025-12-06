

def p1(lines):
    pos,depth = 0,0
    for line in lines:
        dir,val = line.split()
        match dir:
            case "forward":
                pos += int(val)                     
            case "down":
                depth += int(val)            
            case "up":
                depth -= int(val)
    return pos*depth


def p2(lines):
    pos,depth,aim = 0,0,0
    for line in lines:
        dir,val = line.split()
        match dir:
            case "forward":
                pos += int(val)
                depth += aim*int(val)
            case "down":
                aim += int(val)            
            case "up":
                aim -= int(val)
    return pos*depth
    

f = open("input2.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )