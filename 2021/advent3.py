

def p1(lines):
    l= len(lines[0])
    z_l,o_l = [0]*l,[0]*l
    for line in lines:
        ones = [int(x) for x in line]
        zeroes = [1-int(x) for x in line]
        o_l = [sum(x) for x in zip(o_l,ones)]
        z_l = [sum(x) for x in zip(z_l,zeroes)]
    gamma_l = [1 if x>=y else 0 for x,y in zip(o_l,z_l)]
    eps_l = [1 if x<y else 0 for x,y in zip(o_l,z_l)]

    gamma = int("".join(str(x) for x in gamma_l),2)
    eps = int("".join(str(x) for x in eps_l),2)

    return gamma*eps


def p2(lines):
    l= [0]*len(lines[0])
    for line in lines:
        ones = [1 if (int(x) == 1) else -1 for x in line]
        l = [sum(x) for x in zip(l,ones)]
    l = [1 if x>=0 else 0 for x in l]
    gamma_s = "".join(str(x) for x in l)
    eps_s = "".join(str(1-x) for x in l)
    
    ox = lines
    for i in range(len(lines[0])):
        o_0,o_1 = [],[]
        for line in ox:
            if line[i] == '0': o_0.append(line)
            else: o_1.append(line)
        if len(o_1)>= len(o_0): ox = o_1
        else: ox = o_0
        if len(ox) <=1: break

    co2 = lines
    for i in range(len(lines[0])):
        o_0,o_1 = [],[]
        for line in co2:
            if line[i] == '0': o_0.append(line)
            else: o_1.append(line)
        if len(o_0)<= len(o_1): co2 = o_0
        else: co2 = o_1
        if len(co2) <=1: break

    ox_i = int("".join(str(x) for x in ox),2)
    co2_i = int("".join(str(x) for x in co2),2)    
    return ox_i*co2_i
    #return ox,co2
    
f = open("input3.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )