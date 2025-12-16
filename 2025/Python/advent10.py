import timeit


def p1(lines):
    value = 0

    for line in lines:
        indicator_light, button_wirings, joltage_req = (
            line.split(" ")[0],
            line.split(" ")[1:-1],
            line.split(" ")[-1],
        )
        buttons = []
        indicator_size = len(indicator_light) - 2
        goal_state = indicator_light.replace(".", "0").replace("#", "1")[1:-1]
        for wiring in button_wirings:
            current_button = ["0"] * indicator_size
            for wire in wiring[1:-1].split(","):
                current_button[int(wire)] = "1"
            buttons.append("".join(current_button))
        possibilities = []
        for button_mask in range(pow(2, len(button_wirings))):
            pos = 0
            state = 0
            i = button_mask
            while i > 0:
                if i & 1:
                    state ^= int(buttons[pos], 2)
                i >>= 1
                pos += 1
            if state == int(goal_state, 2):
                possibilities.append((bin(button_mask).count("1"), button_mask))

        minimum_presses = min([p[0] for p in possibilities])
        value += minimum_presses

        pass

    return value


def p2(lines):
    value = 0

    for line in lines:
        pass

    return value


# f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/10.input", "r")
lines = [line.strip("\n") for line in f]

start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f"Time: {(stop - start):.4}")
