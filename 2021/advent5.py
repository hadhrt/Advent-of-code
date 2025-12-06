
def p1(lines):
    #read coords
    c=[]
    for line in lines:
        x = line.split()[0::2]
        x = x[0].split(',')+x[1].split(',')
        c.append( list(map(int,x)))
    max_x = max(max(list(zip(*c))[0]),max(list(zip(*c))[2])) +1
    max_y = max(max(list(zip(*c))[1]),max(list(zip(*c))[3])) +1 
    d = [[0]*max_x for i in range(max_y)]

    #draw lines
    for x in c:
        #line
        if x[0] == x[2]:
            if x[1] < x[3]: s,e = x[1],x[3]
            else: s,e = x[3],x[1]
            for i in range(s,e+1): d[i][x[0]]+=1
        #row
        elif x[1] == x[3]:
            if x[0] < x[2]: s,e = x[0],x[2]
            else: s,e = x[2],x[0]
            for i in range(s,e+1): d[x[1]][i]+=1    

    ret = 0
    for l in d:
        for i in l:
            if i>1: ret+=1
    return ret


def print_d(d):

    for i in d:
        print(i)    
    print('')

def p2(lines):
    #read coords
    c=[]
    for line in lines:
        x = line.split()[0::2]
        x = x[0].split(',')+x[1].split(',')
        c.append( list(map(int,x)))
    max_x = max(max(list(zip(*c))[0]),max(list(zip(*c))[2])) +1
    max_y = max(max(list(zip(*c))[1]),max(list(zip(*c))[3])) +1 
    d = [[0]*max_x for i in range(max_y)]

    #draw lines
    for x in c:

        xs = x[2]-x[0]
        xr = abs(xs)
        xs = -1 if xs <-1 else xs
        xs = 1 if xs >1 else xs
        
        ys = x[3]-x[1]
        yr = abs(ys)
        ys = -1 if ys <-1 else ys
        ys = 1 if ys >1 else ys
        
        for i in range(max(xr,yr)+1):
            d[x[1]+i*ys][x[0]+i*xs] +=1


    ret = 0
    for l in d:
        for i in l:
            if i>1: ret+=1
    return ret

    

f = open("input5.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )