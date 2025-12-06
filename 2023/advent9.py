import timeit


def p1(lines):
    values = 0
    final_numbers = []
    for line in lines:
        numbers = [int(number) for number in line.split()]
        rows = []
        all_diffs = []
        current_diffs = numbers.copy()
        while True:
            all_diffs.append(current_diffs.copy())
            current_diffs = [a[1]-a[0] for a in zip(current_diffs,current_diffs[1:])]
            if all([v == 0 for v in current_diffs]): break
        values += sum([v[-1] for v in all_diffs])
        pass


    return values


def p2(lines):
    values = 0
    final_numbers = []
    for line in lines:
        numbers = [int(number) for number in line.split()]
        rows = []
        all_diffs = []
        current_diffs = numbers.copy()
        value = 0
        while True:
            all_diffs.append(current_diffs.copy())
            current_diffs = [a[1]-a[0] for a in zip(current_diffs,current_diffs[1:])]
            if all([v == 0 for v in current_diffs]): break
        
        for diffs in reversed(all_diffs):
            value = diffs[0] - value
        pass
        values += value

    return values
    

f = open("input9.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')