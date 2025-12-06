class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
def adj(r,c):
    ret = [(row,col) for row in range(r-1,r+2) for col in range(c-1,c+2)]
    ret.remove((r,c))
    return ret

def step(grid):

    flashes = 0
    # increase all by 1
    grid = {p:v+1 for p,v in grid.items()}
    # points ready to flash
    flash_queue = {p for p,v in grid.items()if v > 9}
    # already flashed points
    flashed_points = set()
    
    while flash_queue:
        flash_point = flash_queue.pop()
        grid[flash_point] = 0
        flashes += 1
        flashed_points.add(flash_point)
       
        #mark adj points for flash
        for point in adj(*flash_point):
            
            if point in grid:
                #skip if point has already flashed
                if point in flashed_points: continue
                #inc point 
                grid[point] +=1
                #add to flash queue if needed
                if grid.get(point) > 9: flash_queue.add(point)    
    return grid,flashes  


def print_grid(grid):
    r=0
    
    for p,v in grid.items():
        if p[0]>r:
            r = p[0]
            print('')
        if v == 0: print(bcolors.BOLD,end='')
        print(v,end='')
        if v == 0: print(bcolors.ENDC,end='')
    print("\n")
 

 


def p1(lines):
    grid = {(r,c):int(v) for r,line in enumerate(lines) for c,v in enumerate(line)}
    
    flashes_total = 0
    for i in range(100):
        grid,flashes = step(grid)
        flashes_total += flashes
        #print(f"After Step {i+1}:")
        print_grid(grid)
    
    
    return flashes_total

def p2(lines):
    grid = {(r,c):int(v) for r,line in enumerate(lines) for c,v in enumerate(line)}
    
    for i in range(1000):
        grid,flashes = step(grid)
        if flashes == len(grid): 
            #print(f"All flashed at step {i+1}")
            return i+1
           
        #print(f"After Step {i+1}:")
        #print_grid(grid)
    
    
    return None
    
  
f = open("input11.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )