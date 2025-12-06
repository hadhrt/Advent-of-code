

def p1(lines):
    
    grid = {(r,c):int(v) for r,line in enumerate(lines) for c,v in enumerate(line)}

    def visible(p,v):
        return any((
            all([grid.get((rr,p[1])) < v for rr in range(0,p[0])]),
            all([grid.get((rr,p[1])) < v for rr in range(p[0]+1,len(lines[0]))]),
            all([grid.get((p[0],cc)) < v for cc in range(0,p[1])]),
            all([grid.get((p[0],cc)) < v for cc in range(p[1]+1,len(lines))])))
    
    return [visible(p,v) for p,v in grid.items()].count(True)



def p2(lines):

    grid = {(r,c):int(v) for r,line in enumerate(lines) for c,v in enumerate(line)}
    
    def count_line(points,v):
        #print(f"Points: {points} Treehight: {v}")
        ret = 0
        for point in points:
            #print(f"{point}: {grid.get(point)}")
            ret += 1
            if grid.get(point) >= v: 
                break
        #print(f"Return: {ret}")
        return ret

    def visible_trees(p,v):
        return  count_line( [(rr,p[1])for rr in reversed( range(0,p[0]) )]   , v) * \
                count_line( [(rr,p[1])for rr in range(p[0]+1,len(lines[0]))] , v) * \
                count_line( [(p[0],cc)for cc in reversed( range(0,p[1]) )]   , v) * \
                count_line( [(p[0],cc)for cc in range(p[1]+1,len(lines))]    , v)
     
    #return visible_trees((1,2),grid.get((1,2)))
    return max([visible_trees(p,v) for p,v in grid.items()])

    

f = open("input8.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )