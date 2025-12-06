import timeit
import math


def p1(lines):
    value = 0

    problem_list = [[operator, []] for operator in lines[-1].split()]
    for line in lines[:-1]:
        for index, operand in enumerate(line.split()):
            problem_list[index][1].append(int(operand))
    for operator, operand_list in problem_list:
        if operator == "+":
            value += sum(operand_list)
        elif operator == "*":
            value += math.prod(operand_list)
        else:
            return

    return value


def p2(lines):
    answer = 0
    operands = []
    columns = ["".join(c) for c in zip(*lines)]

    for column in columns[::-1]:
        if column.strip() != "":
            operands.append(int(column[:-1]))
            if column[-1] == "+":
                answer += sum(operands)
                operands = []
            elif column[-1] == "*": 
                answer += math.prod(operands)
                operands = []
    return answer


# f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/06.input", "r")
lines = [line.strip("\n") for line in f]

start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")
