import timeit


def p1(lines):
    values = []
    for line in lines:
        line = list(map(int,line))
        first_digit = (0,0)
        second_digit = (0,0)
        
        # first digit is largest digit in line, except at the end of line
        for pos, val in enumerate(line):
            if val > first_digit[1]: 
                first_digit = (pos,val)
                
        # if largest digit is at the end it has to be the second digit
        if first_digit[0] == len(line) - 1:
            second_digit = first_digit
            first_digit = (0,0)
            # find first digit ( = 2nd largest digit)
            for pos, val in enumerate(line[:second_digit[0]]):
                if val > first_digit[1]: 
                    first_digit = (pos,val)
        # find second digit (biggest digit in remaining line)
        else:
            for pos, val in enumerate(line[first_digit[0] + 1:]):
                if val > second_digit[1]: 
                    second_digit = (pos + first_digit[0] + 1,val)
        
        # assemble "joltage" number 
        values.append(int(str(first_digit[1]) + str(second_digit[1])))
    
    return sum(values)


# generalized idea from above
def find_largest_valid_digit(line, starting_pos, remaining_digits):
    digit = (0,0)
    pos = starting_pos
    while len(line) - pos >= remaining_digits:
        if line[pos] > digit[1]: 
            digit = (pos,line[pos])
        pos += 1
    return digit    


def p2(lines):    
    values = []
    for line in lines:
        digits = []
        starting_pos= 0
        line = list(map(int,line))
        
        # find the next largest digit with enough digits remaining in line
        for remaining_digits in range(12,0,-1):
            digit = find_largest_valid_digit(line,starting_pos,remaining_digits)
            starting_pos = digit[0] + 1
            digits.append(digit[1])
            pass
        
        # assemble "joltage" number 
        final_digit_string = ""
        for digit in digits:
            final_digit_string += str(digit)
        values.append(int(final_digit_string))
        
    return sum(values)
        
        

 

#f = open(r"2025/python/Inputs/example.input", "r")
f = open(r"2025/python/Inputs/03.input", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')