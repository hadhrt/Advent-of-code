import timeit
from itertools import pairwise
import numpy as np


def p1(lines):

    numbers = []
    
    for idx,line in enumerate(lines):
        secret_number = int(line)
        sn = secret_number
        for i in range(2000):
            sn = ((sn *64) ^ sn ) % 0x1000000
            sn = ((sn //32) ^ sn ) % 0x1000000
            sn = ((sn *2048) ^ sn ) % 0x1000000
        numbers.append((secret_number,sn))
    return sum([sn[1]for sn in numbers])




def p2(lines):
    # create a dict of all potential sequences and how many bananas they return
    sequence_dict = {}
    
    for line in lines:
        last_digits = []
        secret_number = int(line)
        sn = secret_number
        last_digits.append(sn%10)
        for i in range(2000):
            sn = ((sn *64) ^ sn ) % 0x1000000
            sn = ((sn //32) ^ sn ) % 0x1000000
            sn = ((sn *2048) ^ sn ) % 0x1000000
            last_digits.append(sn%10)
        
        diffs = [d2-d1 for d1,d2 in pairwise(last_digits)]

        sequences_for_this_code = set()
        for i in range(len(diffs) - 4+1):
            seq = tuple(diffs[i:i+4])
            if seq not in sequences_for_this_code:
                sequences_for_this_code.add(seq)
                sequence_dict[seq] = sequence_dict.get(seq,0) + last_digits[i+4]



    return max(sequence_dict.values())
    

f = open("input22.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')