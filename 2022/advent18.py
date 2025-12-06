

def p1(points):

    points = list(points)
    sides = len(points)*6
    
    #print(f"sides initial: {sides}")
    
    for x,y,z in [(0,1,2),(1,2,0),(2,0,1)]:
        points.sort(key = lambda k: k[x])
        for idx,point in enumerate(points):
            i = idx+1
            if i>= len(points): break
            while points[i][x] <= point[x]+1:
                if (point[y] == points[i][y]) and (point[z] == points[i][z]):
                    sides -= 2
                    #print(f"touching points found: {point} - {points[i]}")
                i +=1
                if i>=len(points): break
    
    return sides



def p2(lines):
    
    lava = set()
    for line in lines:
        x,y,z = list(map(int,(line.split(","))))
        lava.add((x,y,z))
    lava_sides = p1(lava)
    print ("Part 1: " + str(lava_sides) )
 
    all_points = set()
    for x in range(20):
        for y in range(20):
            for z in range(20):
                all_points.add((x,y,z)) 
    
    searched = set()
    stack = {(0,0,0)}
    neighbour_coords = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
    
    while stack:
        #print(stack)
        point = stack.pop()
        searched.add(point)
        
        for neighbour in [tuple([sum(x) for x in zip(point,neighbour_coord)]) for neighbour_coord in neighbour_coords]:
            if neighbour[0]< -1 or neighbour[0]> 20: continue
            if neighbour[1]< -1 or neighbour[1]> 20: continue
            if neighbour[2]< -1 or neighbour[2]> 20: continue
            
            if neighbour not in searched and neighbour not in stack and neighbour not in lava:
                stack.add(neighbour)
            
    
    air_pockets = (all_points-searched)-lava
    
    air_sides = p1(air_pockets)
        
            
    return lava_sides-air_sides
    

f = open("input18.txt", "r")
lines = [line.strip() for line in f]
  

#print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )