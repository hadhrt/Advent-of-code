

def p1(line):
    posl =  list(map(int,line.split(',')))
    l = []
    for i in range(max(posl)):
        l.append( sum(abs(x-i) for x in posl))
        #print( f"Position: {i:3d} costs {l[-1]:3d} Fuel")
    return min(l)


def p2(line):
    posl =  list(map(int,line.split(',')))
    l = []
    for i in range(max(posl)):
        
        l.append( sum((abs(x-i)*(abs(x-i) +1))//2 for x in posl))
        #print( f"Position: {i:3d} costs {l[-1]:3d} Fuel")
    return min(l)
    return 0
    

f = open("input7.txt", "r")
line = f.readline()
  

print ("Part 1: " + str(p1(line)) )
print ("Part 2: " + str(p2(line)) )