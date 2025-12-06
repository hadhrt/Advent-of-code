class packet():
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        assert(type(self) == packet)
        assert(type(other) == packet)
        return compare(self.val,other.val)>0
    def __str__(self):
        return str(self.val)
    

def compare(left, right):
    #print(f"Compare {left} vs {right}")
    if type(left) == type(right):
        if type(left) == int:
            #print(f"return based on int: {right - left}")
            return right - left
        if type(left) == list:
            for curr_left, curr_right in zip(left,right):
                cmp = compare(curr_left, curr_right)
                if cmp != 0: return cmp
            #print(f"return based on length: {len(right) - len(right)}")
            return len(right) - len(left)
        assert(False)
    if type(left) == int: return compare([left],right)
    if type(right) == int: return compare(left,[right])

def p1(lines):
    values = 0
    cmps=[]
    for idx,(line_l,line_r) in enumerate(zip(lines[0::3], lines[1::3])):
        left = eval(line_l)
        right = eval(line_r)
        if compare(left,right) > 0: cmps.append(idx+1)
    return sum(cmps)


def p2(lines):
    values = 0
    packets = []
    for line in lines:
        if line != "":
            val = eval(line)
            packets.append(packet(val))
    p2 =  packet([[2]])
    p6 =  packet([[6]])
    packets.append(p2)
    packets.append(p6)
    packets.sort()

    return (packets.index(p2)+1) * (packets.index(p6)+1)

    

f = open("input13.txt", "r")
lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(lines)) )
print ("Part 2: " + str(p2(lines)) )