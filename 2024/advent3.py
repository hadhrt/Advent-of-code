import timeit
import re

def p1(lines):
    values = 0
    for line in lines:
        mul_instructions = re.findall("mul\(\d{1,3},\d{1,3}\)",line)
        for instruction in mul_instructions:
            m1,m2 = re.findall("\d{1,3}", instruction)
            values += int(m1)*int(m2)
    return values


def p2(lines):
    values = 0
    line = "".join(lines)

    ''' long way

    # split the line at any "don't"s
    parts = re.split("don\'t\(\)",line)
    # keep the first part 
    active_line = parts[0]
        # then add remaining string after the first "do()" instruction for each part
    for part in parts[1:]:
        # find first "do()"
        do_instruction = re.search("do\(\)",part)
        # add the part after the "do()" match to the active string
        if do_instruction:
            # add separator to not accidentally create new instructions
            active_line += " "
            active_line += part[do_instruction.span()[1]:]
    '''

    ''' better way '''
    # substitute all parts between a "don't()" and the next "do()", need to use lazy ".*?" matching to get the next "do()" and not a later one
    active_line = re.sub("don\'t\(\).*?do\(\)"," ",line) 


    # find and calculate mul instructions like part 1
    mul_instructions = re.findall("mul\(\d{1,3},\d{1,3}\)",active_line)
    for instruction in mul_instructions:
        m1,m2 = re.findall("\d{1,3}", instruction)
        values += int(m1)*int(m2)

    return values
    

f = open("input3.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')