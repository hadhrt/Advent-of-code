import itertools

def read_input():
    window_values = [0,0]
    with open("input1.txt", "r") as f:
        #First two Windows
        window_values[0] = int(f.readline()[:-1])
        window_values[1] = int(f.readline()[:-1])
        window_values[0] += window_values[1]
        #
        #Middle windows
        for line in f:
            window_values.append(int(line[:-1]))
            window_values[-2] += int(line[:-1])
            window_values[-3] += int(line[:-1])
        #    
        #remove last 2 unfinished Windows
        window_values.pop()    
        window_values.pop() 
        #
    return window_values


window_values =  read_input()
num_increases = 0
for i,j in itertools.pairwise(window_values):
    if j>i: num_increases +=1
    
print ("Number of increases: " + str(num_increases))
