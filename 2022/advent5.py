
from collections import deque


def p1(lines):
    #Größe ermitteln
    num_stacks = 0
    size_stacks = 0
    for line in lines:
        if line.find("1") != -1:
            size_stacks = lines.index(line)
            num_stacks = len(line)//4
            break
    stacks = [deque([]) for a in range(num_stacks)]
    
    #Stacks einlesen
    for i in range(size_stacks-1,-1,-1):
        for j in range(num_stacks):
            if lines[i][4*j+1] != " ":
                stacks[j].append(lines[i][4*j+1])
    #moves isolieren
    lines = lines[size_stacks+2:]

    #moves durchführen
    for line in lines:
        move = line.split()
        for i in range(int(move[1])):
            stacks[int(move[5])-1].append(stacks[int(move[3])-1].pop())
    
    ret = ''.join([i.pop() for i in stacks])
    return ret


def p2(lines):
    #Größe ermitteln
    num_stacks = 0
    size_stacks = 0
    for line in lines:
        if line.find("1") != -1:
            size_stacks = lines.index(line)
            num_stacks = len(line)//4
            break
    stacks = [[] for i in range(num_stacks)]
    
    #Stacks einlesen
    for i in range(size_stacks-1,-1,-1):
        for j in range(num_stacks):
            if lines[i][4*j+1] != " ":
                stacks[j].append(lines[i][4*j+1])
    #moves isolieren
    lines = lines[size_stacks+2:]
    
    #moves durchführen
    for line in lines:
        move = line.split()
        num,fr,to = int(move[1]),int(move[3])-1,int(move[5])-1

        stacks[to] += stacks[fr][-num:]
        stacks[fr] =  stacks[fr][:-num]
    
    ret = ''.join([i[-1] for i in stacks])
    return ret
    

f = open("input5.txt", "r")
lines = [line for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )