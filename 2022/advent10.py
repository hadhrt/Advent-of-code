

def p1(lines):
    values = 0
    x = [1,1]
    for line in lines:
        if line == "noop":
            x.append(x[-1])
        else:
            cmd, val = line.split()
            if cmd == "addx":
                x.append(x[-1])
                x.append(x[-1] + int(val) )
    
    vals = [20,60,100,140,180,220]
    sum = 0
    for val in vals:
       sum += x[val] * val 
    
    return sum

def p2(lines):
    values = 0
    x = [1]
    crt_str = ""
    for line in lines:
        if line == "noop":
            x.append(x[-1])
        else:
            cmd, val = line.split()
            if cmd == "addx":
                x.append(x[-1])
                x.append(x[-1] + int(val) )
    for j in range(6):
        for i in range(40):
            print(f"i: {i} x: {x[i]} hit: {i in (x[i]-1, x[i], x[i]+1)}")
            if i in (x[40*j+i]-1, x[40*j+i], x[40*j+i]+1):
                crt_str += "#"
            else:
                crt_str += "." 
        crt_str +="\n"
    return crt_str
    

f = open("input10.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: \n" + str(p2(lines)) )
