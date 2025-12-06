import timeit
import math

ADJ_OFFSETS = (-1 - 1j, -1 + 0j, -1 + 1j, 0 - 1j, 0 + 1j, 1 - 1j, 1 + 0j, 1 + 1j)

ADJ_OFFSETS_NO_DIAG = (
    -1 + 0j,
    0 - 1j,
    0 + 1j,
    1 + 0j,
)


def print_grid(grid):
    print_string = ""
    for coord, val in grid.items():
        if coord.imag == 0:
            print_string += "\n"
        print_string += val
    print(print_string)


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
    value = 0
    numbers = [
        int("".join(numberstring).strip())
        for numberstring in list(zip(*map(list, lines[:-1])))
        if "".join(numberstring).strip() != ""
    ]
    # operator line defines the amount of numbers per problem
    # split string at operands but keep operands by inserting magic value as separator
    operators = [
        (operator_string[0], len(operator_string) - 1)
        for operator_string in (
            lines[-1].replace("+", "¬¬+").replace("*", "¬¬*") + " "
        ).split("¬¬")[1:]
    ]

    numberiter = iter(numbers)
    for operator in operators:
        problem_numbers = [next(numberiter) for _ in range(operator[1])]
        if operator[0] == "+":
            value += sum(problem_numbers)
        elif operator[0] == "*":
            value += math.prod(problem_numbers)
        else:
            return

    return value


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
