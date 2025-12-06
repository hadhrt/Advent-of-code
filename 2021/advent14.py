import timeit
from collections import Counter


def p1(lines):
    str = lines[0]
    lines = lines[2:]
    insert_dict = {}
    for line in lines:
        pair, insertion = line.split(" -> ")
        insert_dict[pair] = insertion
    steps = 10
    for i in range(steps):
        str = process_string(str, insert_dict)
        #print(f"After {i+1} steps: Length = {len(str)}")
    charcounter = Counter(str)
    most_common = charcounter.most_common()[0][1]
    least_common = charcounter.most_common()[-1][1]

    return most_common - least_common


def process_string(str, insert_dict):
    newstr = ""
    pair = "  "
    for char in str:
        newstr += pair[1]
        pair = pair[1:]+char
        newstr += insert_dict.get(pair, "")
    newstr = newstr[1:]+pair[1]
    return newstr


def p2(lines):
    str = lines[0]
    lines = lines[2:]
    insert_dict = {}
    for line in lines:
        pair, insertion = line.split(" -> ")
        insert_dict[pair] = [pair[0] + insertion, insertion + pair[1]]


    counter_dict = {}
    for p1,p2 in zip(str[0:],str[1:]):
        counter_dict[p1+p2] = counter_dict.get(p1+p2,0)+1 
    for i in range(40):
        new_counter_dict = {}
        for pair, count in counter_dict.items():
            if pair in insert_dict:
                new_pairs = insert_dict.get(pair)
                new_counter_dict[new_pairs[0]] = new_counter_dict.get(new_pairs[0],0) + count
                new_counter_dict[new_pairs[1]] = new_counter_dict.get(new_pairs[1],0) + count
            else:
                new_counter_dict[pair] = new_counter_dict.get(pair,0) + count
        counter_dict = new_counter_dict
        #print(counter_dict)
    char_counter = {}
    # every char is the first char of a pair except the very last char
    for pair, count in counter_dict.items():
        char_counter[pair[0]] = char_counter.get(pair[0],0) + count
    char_counter[str[-1]] = char_counter[str[-1]] +1

    #print(char_counter)
    sorted_char_counter_list = sorted(list(char_counter.items()),key=lambda x:x[1], reverse=True)
    #print(sorted_char_counter_list)
    return sorted_char_counter_list[0][1]-sorted_char_counter_list[-1][1]

f = open("input14.txt", "r")
lines = [line.strip() for line in f]


start = timeit.default_timer()
print(f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)
