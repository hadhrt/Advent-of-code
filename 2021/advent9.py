

def p1(lines):
    v = []
    m = [[9]*(len(lines[0])+2)]
    for line in lines:
        m.append([9]+list(map(int,list(line)))+[9])
    m.append([9]*(len(line)+2))
    #print(m)
    
    for ir,r in enumerate(m[1:-1]):
        for ic,c in enumerate(r[1:-1]):
            if m[ir+0][ic+1] > c and \
               m[ir+2][ic+1] > c and \
               m[ir+1][ic+0] > c and \
               m[ir+1][ic+2] > c:
               #print("Lowpoint:")
               v.append(c)
            #print(c, m[ir-1][ic], m[ir+1][ic],m[ir][ic-1],m[ir][ic+1])
    return sum(map(lambda x: x+1,v))


def p2(lines):
    lowpoints = []
    m = [[9]*(len(lines[0])+2)]
    for line in lines:
        m.append([9]+list(map(int,list(line)))+[9])
    m.append([9]*(len(line)+2))
    #print(m)
    
    for ir,r in enumerate(m[1:-1]):
        for ic,c in enumerate(r[1:-1]):
            if m[ir+0][ic+1] > c and \
               m[ir+2][ic+1] > c and \
               m[ir+1][ic+0] > c and \
               m[ir+1][ic+2] > c:
               #print("Lowpoint:")
               lowpoints.append(((ir+1),(ic+1)))
            #print(c, m[ir-1][ic], m[ir+1][ic],m[ir][ic-1],m[ir][ic+1])

    for idx,lp in enumerate(lowpoints):
        size = 0
        visited=[]
        candidates=[lp]
        while len(candidates) > 0:
            #print(candidates)
            c = candidates.pop()
            visited.append(c)
            size += 1
            for nc in [(c[0]-1,c[1]),(c[0]+1,c[1]),(c[0],c[1]-1),(c[0],c[1]+1)]:
                if nc not in visited and nc not in candidates and m[nc[0]][nc[1]] != 9 and m[nc[0]][nc[1]] > m[c[0]][c[1]]:
                    candidates.append(nc)
        lowpoints[idx] = lp + (size,)
    prod = 1
    bas = [x for _,_,x in lowpoints]
    for x in sorted(bas,reverse=True)[:3]: prod *= x

    return (sorted(bas,reverse=True)[:3],prod)



f = open("input9.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )