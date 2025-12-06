import timeit
from collections import defaultdict
from math import floor,log10


def p1(lines):
    values = 0
    numbers = defaultdict(int)

    for number in map(int,lines[0].split()):
        numbers[number] = 1

    for i in range(25):
        numbers = step(numbers)

    return sum([amount for _,amount in numbers.items()])

def step_math(numbers):
    new_numbers = defaultdict(int)
    for number, amount in numbers.items():
        if number == 0:
            new_numbers[1] = new_numbers[1] + amount
            continue
        l = floor(log10(number))+1
        if l % 2 == 0:
            n1 = number // 10**(l//2)
            n2 = number %  10**(l//2)
            new_numbers[n1] = new_numbers[n1] + amount
            new_numbers[n2] = new_numbers[n2] + amount
        else:
            new_numbers[number*2024] = new_numbers[number*2024] + amount
    return new_numbers


def step(numbers):
    new_numbers = defaultdict(int)
    for number, amount in numbers.items():
        if number == 0:
            new_numbers[1] = new_numbers[1] + amount
        elif len(str(number))%2 == 0:
            num_str = str(number)
            n1, n2 = int(num_str[:len(num_str)//2]), int(num_str[len(num_str)//2:])
            new_numbers[n1] = new_numbers[n1] + amount
            new_numbers[n2] = new_numbers[n2] + amount
        else:
            new_numbers[number*2024] = new_numbers[number*2024] + amount
    return new_numbers

def p2(lines):
    values = 0
    numbers = defaultdict(int)

    for number in map(int,lines[0].split()):
        numbers[number] = 1

    for i in range(75):
        numbers = step(numbers)

    return sum([amount for _,amount in numbers.items()])

f = open("input11.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')