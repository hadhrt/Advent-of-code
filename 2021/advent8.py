

def p1(lines):
    value = 0
    for line in lines:
        _,l = line.split('|')
        ls = [len(x) for x in l.split()]
        ls = list(map(lambda x: 1 if x == 2 or x == 4 or x == 3 or x == 7 else 0 ,ls))
        value += sum(ls)
    return value


def p2(lines):
    values = 0
    for line in lines:
        d, output = [x.split() for x in line.split('|')]
        d = [set(x) for x in d]
        output = [set(x) for x in output]
        digit = [None]*10
        
        
        d.sort(key = len)
        digit[1] = d[0]
        digit[7] = d[1]
        digit[4] = d[2]
        digit[8] = d[9]
        
        s5 = d[3:6]
        s6 = d[6:9]

        #9: 6 segment digit with 4 segments that are also in digit 4
        for x in s6: 
            if (len(x.intersection(digit[4])) == 4):
                digit[9] = x
                s6.remove(x)
        #3: 5 segment digit with 2 segments that are also in digit 1
        for x in s5: 
            if (len(x.intersection(digit[1])) == 2):
                digit[3] = x
                s5.remove(x)
        #5: 5 segment digit with 5 segments that are also in digit 9
        for x in s5: 
            if (len(x.intersection(digit[9])) == 5):
                digit[5] = x
                s5.remove(x)
        #2: remaining 5 segment digit
        digit[2] = s5.pop()
        #6: 6 segment digit with 5 segments that are also in digit 5
        for x in s6: 
            if (len(x.intersection(digit[5])) == 5):
                digit[6] = x
                s6.remove(x)
        #0: remaining 6 segment digit
        digit[0] = s6.pop()
        
        values += int(''.join([str(digit.index(o)) for o in output]))
        
        
        

           
    return values
    

f = open("input8.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )