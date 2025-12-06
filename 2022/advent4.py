

def p1(lines):
    values = 0
    for line in lines:
        lv = [int(x) for x in line.replace('-',',').split(',')]
        if (lv[0]-lv[2])*(lv[1]-lv[3]) <= 0: values+=1 
    return values


def p2(lines):
    values = 0
    for line in lines:
        lv = [int(x) for x in line.replace('-',',').split(',')]
        if (lv[1]>=lv[2] and lv[0]<=lv[3]): values+=1 
    return values
    
f = open("input4.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )