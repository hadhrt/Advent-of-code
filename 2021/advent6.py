


def p1(line):
    num_days = 80
    lfs =  list(map(int,line.split(',')))
    for days in range(num_days):
        for i in range(len(lfs)):
            if lfs[i] > 0 : lfs[i] -= 1
            elif lfs[i] == 0:
                lfs[i] = 6
                lfs.append(8)
        #print(f"After {days+1:2d} days: {len(lfs)} Fish")
    return len(lfs)


    
    
    
def p2(line):
    num_days = 256
    lfs =  list(map(int,line.split(',')))
    
    fishes = [0]*9
    
    for lf in lfs:
        fishes[lf] += 1
        
    
    
    for days in range(num_days):
        fish_0 = fishes[0]
        #age fish
        fishes = fishes[1:] + [0]
        #process "0" day fishes
        fishes[6] += fish_0
        fishes[8] += fish_0

        
        #print(f"After {days+1:2d} days: {sum(fishes)} Fish: {fishes}")
    return sum(fishes)

    

f = open("input6.txt", "r")
line = f.readline()
  

print ("Part 1: " + str(p1(line)) )
print ("Part 2: " + str(p2(line)) )