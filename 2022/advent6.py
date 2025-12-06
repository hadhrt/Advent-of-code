from collections import deque

def p1(fn):
    f = open(fn, "r")
    line = f.read()
    buffer = deque([c for c in line])
    buffer_4 = deque([])
    num_rec = 0
    
    while(len(buffer_4) < 4):
        #print(buffer_4)
        c = buffer.popleft()
        num_rec += 1
        if c in buffer_4: 
            while buffer_4.popleft() != c: pass
        buffer_4.append(c)
        
    return num_rec


def p2(lines):
    f = open(fn, "r")
    line = f.read()
    buffer = deque([c for c in line])
    buffer_14 = deque([])
    num_rec = 0
    
    while(len(buffer_14) < 14):
        #print(buffer_4)
        c = buffer.popleft()
        num_rec += 1
        if c in buffer_14: 
            while buffer_14.popleft() != c: pass
        buffer_14.append(c)
        
    return num_rec
    

fn = "input6.txt"
#lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(fn)) )
print ("Part 2: " + str(p2(fn)) )