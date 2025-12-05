import timeit
import math


def primeFactors(N):
    p,i = 2,1               # prime divisor and increment
    while p*p<=N:           # no need to go beyond √N 
        while N%p == 0:     # if is integer divisor
            yield p         # output prime divisor
            N //= p         # remove it from the number
        p,i = p+i,2         # advance to next potential divisor 2, 3, 5, ... 
    if N>1: yield N         # remaining value is a prime if not 1



def p1(lines):
    value = 0
    line = lines[0]

    range_strings = line.split(",")  
    id_ranges = [tuple(map(int,(range_string.split("-")))) for range_string in range_strings]

    invalid_ids = set()
    #range_sizes = [end_ID- start_ID for start_ID,end_ID in id_ranges]
    for start_ID,end_ID in id_ranges:  
        half_ids_to_check = set()      
        for id in range(start_ID, end_ID+1):
            if len(str(id)) % 2 ==1:
                continue
            half_ids_to_check.add(int(str(id)[:len(str(id))//2]))
        for half_id in half_ids_to_check:
            if int(str(half_id)+str(half_id)) in range(start_ID, end_ID+1):
                invalid_ids.add(int(str(half_id)+str(half_id)))

    return sum(invalid_ids)


def p2(lines):
    value = 0

    line = lines[0]
    range_strings = line.split(",")  
    id_ranges = [tuple(map(int,(range_string.split("-")))) for range_string in range_strings]

    invalid_ids = set()
    
    for start_ID,end_ID in id_ranges:
        for id in range(start_ID, end_ID+1):
            # possible number of sequences
            unique_prime_factors = set(primeFactors(len(str(id))))
            # is number[first sequence(1/n) repeated n times] in range?
            for factor in unique_prime_factors:
                sequence_repeating_number = int(str(id)[:len(str(id))//factor] * factor)
                if sequence_repeating_number in range(start_ID, end_ID+1):
                    invalid_ids.add(sequence_repeating_number)
              
            
    pass                      
    return sum(invalid_ids)
 

#f = open(r"2025/Inputs/example.input", "r")
f = open(r"2025/Inputs/02.input", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')