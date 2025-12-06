
def p1(lines):
    dir_map = {'R':1,'L':-1,'U':0+1j,'D':0-1j}
    values = 0
    H = 0+0j
    T = 0+0j
    visited = {T}
    for line in lines:
        #print("\n== " + line + " ==\n")
        dir, steps = line.split()
        for step in range(int(steps)):
            H += dir_map.get(dir)
            T += get_dir(H,T)
            visited.add(T)
            #printgrid(H,T)             
    #print_visited(visited)
    return len(visited)
    
def get_dir(H,T):
    if abs(H-T)>=2:
        real = int(H.real-T.real)
        imag = int(H.imag-T.imag)
        if real > 1: real = 1
        if real < -1: real = -1
        if imag > 1: imag = 1
        if imag < -1: imag = -1
        return complex(real,imag)
    else: return(0+0j)

   
def p2(lines):
    dir_map = {'R':1,'L':-1,'U':0+1j,'D':0-1j}
    values = 0
    H = 0+0j
    snake = [0+0j]*9
    visited = {H}
    for line in lines:
        #print("\n== " + line + " ==\n")
        dir, steps = line.split()
        for step in range(int(steps)):
            H += dir_map.get(dir)
            lead = H
            for idx, point in enumerate(snake):
                snake[idx] += get_dir(lead,point)
                lead = snake[idx] 
            visited.add(snake[8])
        #printgrid_snake(H,snake)

    print_visited(visited)
    return len(visited)

    

def print_visited(visited):
    row_min = int(min([p.imag for p in visited]))
    row_max = int(max([p.imag for p in visited]))
    col_min = int(min([p.real for p in visited]))
    col_max = int(max([p.real for p in visited]))
    
    for r in reversed(range(row_min,row_max+1)):
        print('')
        for c in range(col_min,col_max+1):
            if complex(c,r) in visited: print('#',end='')
            else: print('.',end='')
    print('')
    
def printgrid(H,T): 
    for r in range(5):
        print('')
        for c in range(6):
            if int(T.real) == c and int(T.imag) == 4-r : print('T',end='')
            elif int(H.real) == c and int(H.imag) == 4-r : print('H',end='')
            else: print('.',end='')         
    print('')

def printgrid_snake(H,snake): 
    for r in reversed(range(-5,16)):
        print('')
        for c in range(-11,15):
            printed = False
            if int(H.real) == c and int(H.imag) == r : 
                print('H',end='')
                printed = True
            for i,p in enumerate(snake):
                if int(p.real) == c and int(p.imag) == r : 
                    print(str(i+1),end='')
                    printed = True
                    break
            if r == 0 and c == 0 and not printed : 
                print('s',end='')
                printed = True
            if not printed: print('.',end='')         
    print('')    
    
f = open("input9.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )