import curses



def main(stdscr):
    
    
    f = open("input.txt", "r")
    lines = [line.strip() for line in f]
    grid = {(r,c):int(v) for r,line in enumerate(lines) for c,v in enumerate(line)}
    curses.curs_set(0) # make cursor invisible
    # normal
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # ready to flash
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # flashed
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # flashing
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)
    # flashing
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_WHITE)

    #stdscr.addstr(0,0,"This is BLINK",curses.A_BLINK)
    #stdscr.refresh()
    #stdscr.getkey()
    
    print_grid(stdscr,grid)
    stdscr.getkey()
    
    for i in range(10):
        grid = show_step(stdscr,grid)
        stdscr.getkey()
    
    
    return


def print_grid(stdscr,grid):

    # print grid
    for p,v in grid.items():
        stdscr.addstr(*p,str(v),curses.color_pair(1))
    stdscr.refresh()
    return
    
    
def adj(r,c):
    ret = [(row,col) for row in range(r-1,r+2) for col in range(c-1,c+2)]
    ret.remove((r,c))
    return ret

def show_step(stdscr,grid):

    UPDATE_SPEED_GRID = 1
    FLASH_SPEED = 40
    WAIT_BEFORE_FLASH = 150
    WAIT_AFTER_FLASH = 80
    WAIT_BEFORE_NEW_GRID = 80
    

    for p,v in grid.items():
        stdscr.addstr(*p,str(v),curses.color_pair(1))
    stdscr.refresh()
    curses.napms(WAIT_BEFORE_NEW_GRID)
    
    for p,v in grid.items():
        stdscr.addstr(*p,str(v),curses.color_pair(5))
    stdscr.refresh()
    curses.napms(FLASH_SPEED*3)
    
    flashes = 0
  
    # increase all by 1
    grid = {p:v+1 for p,v in grid.items()}

    # show updating of grid
    for p,v in grid.items():
        if v > 9:
            stdscr.addstr(*p,"X",curses.color_pair(2)) #ready to flash
        else:
            stdscr.addstr(*p,str(v),curses.color_pair(1)) #normal
    stdscr.refresh()
    

    # points ready to flash
    flash_queue = {p for p,v in grid.items()if v > 9}
    # already flashed points
    flashed_points = set()
    
    while flash_queue:
        flash_point = flash_queue.pop()
        grid[flash_point] = 0
        flashes += 1
        flashed_points.add(flash_point)
       
        # animate flashing point
        stdscr.addstr(*flash_point,'X',curses.color_pair(4)) #flashing
        stdscr.refresh()
        curses.napms(WAIT_BEFORE_FLASH) 

        #flash adj points
        for point in adj(*flash_point):
            if point in grid:
               
                # animate flashing point 
                if grid[point] > 9:
                    stdscr.addstr(*point,"X",curses.color_pair(4))
                    
                # animate normal point
                else:
                    stdscr.addstr(*point,str(grid.get(point)),curses.color_pair(5))

        stdscr.refresh()
        curses.napms(FLASH_SPEED)

        #mark adj points for flash
        for point in adj(*flash_point):
            if point in grid:

                 
                #inc point if not flashed
                if point not in flashed_points: grid[point] +=1
                
                
                # animate flash point and add to flash queue
                if grid[point] > 9:
                    stdscr.addstr(*point,"X",curses.color_pair(2)) #ready to flash
                    if point not in flashed_points: flash_queue.add(point)
                    
                # animate flashed point    
                elif grid[point] == 0:
                    stdscr.addstr(*point,str(grid.get(point)),curses.color_pair(3)) #flashed

                # animate normal point
                else:
                    stdscr.addstr(*point,str(grid.get(point)),curses.color_pair(1)) #normal


                    
        stdscr.refresh()
        curses.napms(WAIT_AFTER_FLASH)                    
             
        stdscr.addstr(*flash_point,str(grid.get(flash_point)),curses.color_pair(3)) #flashed
     

    return grid


 


def p1(lines):
    grid = {(r,c):int(v) for r,line in enumerate(lines) for c,v in enumerate(line)}
    
    flashes_total = 0
    for i in range(100):
        #grid,flashes = step(grid)
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
    


curses.wrapper(main)

 
f = open("input.txt", "r")
lines = [line.strip() for line in f]
  

#print ("Part 1: " + str(p1(lines)) )
#print ("Part 2: " + str(p2(lines)) )