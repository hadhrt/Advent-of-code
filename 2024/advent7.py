import timeit
import collections

def p1(lines):  
    values = 0
    for line in lines:
        target_str,remaining_line = line.split(":")
        target = int(target_str)
        operands = tuple(map(int,remaining_line.split()))
        if calc(operands[1:], operands[0],target) == True:
            values += target
    return values

def calc(remaining_operands, current_value, target, p2=False):
    if len(remaining_operands) == 0:
        if current_value == target:
            return True
        else:
            return False
    else:
        if p2:
             return calc(remaining_operands[1:], current_value + remaining_operands[0], target, p2=True) or calc(remaining_operands[1:], current_value * remaining_operands[0], target, p2=True) or calc(remaining_operands[1:], int(f"{current_value}{remaining_operands[0]}"), target, p2=True)

        else:
            return calc(remaining_operands[1:], current_value + remaining_operands[0], target) or calc(remaining_operands[1:], current_value * remaining_operands[0], target)


def p2(lines):
    values = 0
    for line in lines:
        target_str,remaining_line = line.split(":")
        target = int(target_str)
        operands = tuple(map(int,remaining_line.split()))
        if calc(operands[1:], operands[0],target, p2=True) == True:
            values += target
    return values


f = open("input7.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')