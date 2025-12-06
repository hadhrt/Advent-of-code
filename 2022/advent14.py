

def p1(lines):

    col_max = 0 
    row_max = 0
    for line in lines:
        for point in line.split("->"):
            col,row = map(int,point.split(","))
            if col > col_max: col_max = col
            if row > row_max: row_max = row
    grid = {(col,row): "." for row in range(row_max+1) for col in range(col_max+1)}     
    for line in lines:
        points = line.split("->")
        for p1_s,p2_s in zip(points[0::1], points[1::1]):
            p1c,p1r = map(int,p1_s.split(","))
            p2c,p2r = map(int,p2_s.split(","))
            
            if p1c == p2c:
                fro = min(p1r,p2r)
                to = max(p1r,p2r)+1
                for row in range(fro,to):
                    grid[(p1c,row)] = "#"
                
            if p1r == p2r:
                fro = min(p1c,p2c)
                to = max(p1c,p2c)+1
                for col in range(fro,to):
                    grid[(col,p1r)] = "#"      
    
    pos = (500,0)
    i = 0
    while step_sand(grid,pos,row_max):
        #print_grid(grid,col_max,row_max)
        i+=1        
        
    return i

def print_grid(grid,col_max,row_max):
    for row in range(row_max+1):
        print("")
        for col in range(col_max+1):
            print(str(grid[(col,row)]), end='')
    print("")

def step_sand(grid,pos,row_max):
    #abyss reached:
    if pos[1] == row_max:
        return False
    #fall down
    if grid.get((pos[0],pos[1]+1),"~") == ".":
        return step_sand(grid,(pos[0],pos[1]+1),row_max)
    elif grid.get((pos[0]-1,pos[1]+1),"~") == ".":
        return step_sand(grid,(pos[0]-1,pos[1]+1),row_max)
    elif grid.get((pos[0]+1,pos[1]+1),"~") == ".":
        return step_sand(grid,(pos[0]+1,pos[1]+1),row_max)
    #rest here
    else:
        grid[pos]="o"
        return True
        
def step_sand_2(grid,pos,row_max):
    #fall down
    if grid.get((pos[0],pos[1]+1),"~") == ".":
        return step_sand(grid,(pos[0],pos[1]+1),row_max)
    elif grid.get((pos[0]-1,pos[1]+1),"~") == ".":
        return step_sand(grid,(pos[0]-1,pos[1]+1),row_max)
    elif grid.get((pos[0]+1,pos[1]+1),"~") == ".":
        return step_sand(grid,(pos[0]+1,pos[1]+1),row_max)
    elif grid[pos] == "o":
        return False
    #rest here
    else:
        grid[pos]="o"
        return True
        
        
def p2(lines):

    col_max = 1000
    row_max = 0
    for line in lines:
        for point in line.split("->"):
            col,row = map(int,point.split(","))
            if row > row_max: row_max = row
    row_max += 2
    grid = {(col,row): "." for row in range(row_max+1) for col in range(col_max+1)}     
    for line in lines:
        points = line.split("->")
        for p1_s,p2_s in zip(points[0::1], points[1::1]):
            p1c,p1r = map(int,p1_s.split(","))
            p2c,p2r = map(int,p2_s.split(","))
            
            if p1c == p2c:
                fro = min(p1r,p2r)
                to = max(p1r,p2r)+1
                for row in range(fro,to):
                    grid[(p1c,row)] = "#"
                
            if p1r == p2r:
                fro = min(p1c,p2c)
                to = max(p1c,p2c)+1
                for col in range(fro,to):
                    grid[(col,p1r)] = "#"      
    for col in range(col_max+1):
        grid[(col,row_max)] = '#'
    
    pos = (500,0)
    i = 0
    while step_sand_2(grid,pos,row_max):
        #print_grid(grid,col_max,row_max)
        i+=1        
        
    return i

f = open("input14.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )