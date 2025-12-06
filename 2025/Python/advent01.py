import timeit


def p1(lines):
    current_pos = 50
    pos_list = [current_pos]

    # calculate list of dial positions
    for line in lines:
        if line[0] == "R":
            current_pos = (current_pos + int(line[1:])) % 100
        elif line[0] == "L":
            current_pos = (current_pos - int(line[1:])) % 100
        else:
            return -1
        pos_list.append(current_pos)

    # return number of times where dial is left pointing at 0
    return pos_list.count(0)


def p2(lines):
    current_pos = 50
    clicks = 0

    for line in lines:
        dial_amount = int(line[1:])

        # count full rotations
        if dial_amount >= 100:
            clicks += dial_amount // 100
            dial_amount %= 100

        # process remaining partial rotation
        if line[0] == "R":
            current_pos += dial_amount
            if current_pos >= 100:
                clicks += 1
                current_pos %= 100
        elif line[0] == "L":
            # no click if starting at 0
            if current_pos == 0:
                current_pos = (current_pos - dial_amount) % 100
            else:
                current_pos -= dial_amount
                if current_pos <= 0:
                    clicks += 1
                    current_pos %= 100
        else:
            return -1

    return clicks


# f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/01.input", "r")

lines = [line.strip() for line in f]

start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")
