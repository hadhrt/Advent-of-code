value_index = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1(lines):
    values = 0
    for line in lines:
        m = len(line)//2
        a = set(line[:m])
        b = set(line[m:])
        item = (a&b).pop()
        value = value_index.index(item)   
        values += value
    return values


def p2(lines):
    values = 0
    for l1,l2,l3 in zip(lines[0::3],lines[1::3],lines[2::3]):
        item = (set(l1)&set(l2)&set(l3)).pop()
        value = value_index.index(item)     
        values += value
    return values
    

f = open("input3.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )