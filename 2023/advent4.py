import timeit
from collections import deque

def p1(lines):
    values = 0
    for line in lines:
        half_0,half_1 = line.split("|")
        my_numbers =  map(int,half_1.split())
        winning_numbers = map(int,half_0.split(":")[1].split())
        matching_numbers = set(my_numbers) & set(winning_numbers)
        if len(matching_numbers) >0:
            values += pow(2,len(matching_numbers)-1)
    return values


def p2(lines):
    tickets = [1]* len(lines)
    for line_idx,line in enumerate(lines):
        if tickets[line_idx] <= 0:
            continue
        half_0,half_1 = line.split("|")
        my_numbers =  map(int,half_1.split())
        _,winning_number_s = half_0.split(":")
        winning_numbers = map(int,winning_number_s.split())
        matching_numbers = set(my_numbers) & set(winning_numbers)
        for i in range(len(matching_numbers)):
            if line_idx+i+1 < len(tickets):
                tickets[line_idx+i+1] += tickets[line_idx]

    return sum(tickets)



f = open("input4.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')