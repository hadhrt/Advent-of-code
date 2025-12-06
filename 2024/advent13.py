import timeit
from itertools import batched
from dataclasses import dataclass
from math import inf
import numpy as np
import copy

@dataclass
class Clawmachine:
    button_a_offset:complex
    button_b_offset:complex
    price_coord:complex
    cheapest_win:tuple[int,int,int]

def p1(lines):

    clawmachines = []
    for line_quartett in batched(lines,4):
        _,a_X_str,a_Y_str = line_quartett[0].split("+")
        a_X = int(a_X_str.split(",")[0])
        a_Y = int(a_Y_str)
        _,b_X_str,b_Y_str = line_quartett[1].split("+")
        b_X = int(b_X_str.split(",")[0])
        b_Y = int(b_Y_str)
        _,price_X_str,price_Y_str = line_quartett[2].split("=")
        price_X = int(price_X_str.split(",")[0])
        price_Y = int(price_Y_str)       
        clawmachines.append(Clawmachine(button_a_offset=complex(a_X,a_Y), button_b_offset=complex(b_X,b_Y), price_coord=complex(price_X,price_Y), cheapest_win=(inf,inf,inf)))

    # brute_force_cheapest_wins(clawmachines)
    calculate_cheapest_wins(clawmachines)
    # calculate_cheapest_wins_numpy(clawmachines)

    return sum([clawmachine.cheapest_win[2] for clawmachine in clawmachines if clawmachine.cheapest_win[2] < inf])

def brute_force_cheapest_wins(clawmachines):
    for clawmachine in clawmachines:
        for a in range(101):
            a_coord = a * clawmachine.button_a_offset
            if a_coord.real > clawmachine.price_coord.real or a_coord.imag > clawmachine.price_coord.imag:
                    break
            for b in range(101):
                b_coord = b * clawmachine.button_b_offset
                if a_coord.real + b_coord.real > clawmachine.price_coord.real or a_coord.imag + b_coord.imag > clawmachine.price_coord.imag:
                    break
                if (a * clawmachine.button_a_offset) + (b * clawmachine.button_b_offset) == clawmachine.price_coord:
                    if 3*a+b < clawmachine.cheapest_win[2]:
                        clawmachine.cheapest_win = (a,b,3*a+b)
                        break
    return

def p2(lines):
    clawmachines = []
    for line_quartett in batched(lines,4):
        _,a_X_str,a_Y_str = line_quartett[0].split("+")
        a_X = int(a_X_str.split(",")[0])
        a_Y = int(a_Y_str)
        _,b_X_str,b_Y_str = line_quartett[1].split("+")
        b_X = int(b_X_str.split(",")[0])
        b_Y = int(b_Y_str)
        _,price_X_str,price_Y_str = line_quartett[2].split("=")
        price_X = int(price_X_str.split(",")[0]) + 10000000000000
        price_Y = int(price_Y_str) + 10000000000000
        clawmachines.append(Clawmachine(button_a_offset=complex(a_X,a_Y), button_b_offset=complex(b_X,b_Y), price_coord=complex(price_X,price_Y), cheapest_win=(inf,inf,inf)))


    calculate_cheapest_wins_numpy(clawmachines)

    return sum([clawmachine.cheapest_win[2] for clawmachine in clawmachines if clawmachine.cheapest_win[2] < inf])


def calculate_cheapest_wins_numpy(clawmachines):
    for clawmachine in clawmachines:
        eqs = np.array([[clawmachine.button_a_offset.real, clawmachine.button_b_offset.real], [clawmachine.button_a_offset.imag, clawmachine.button_b_offset.imag]]) 
        res = np.array([clawmachine.price_coord.real, clawmachine.price_coord.imag])

        x = np.linalg.solve(eqs,res).round()
        if all(eqs @ x == res) :
            clawmachine.cheapest_win = (int(x[0]),int(x[1]),3*int(x[0])+int(x[1]))



def calculate_cheapest_wins(clawmachines):
    for clawmachine in clawmachines:

        # A * a_X + B * b_X = price_X
        # A * a_Y + B * b_Y = price_Y

        # A = (price_X - (B * b_X)) / a_X
        # A = (price_Y - (B * b_Y)) / a_Y

        # (price_X - (B * b_X)) / a_X = (price_Y - (B * b_Y)) / a_Y
        # (price_X - (B * b_X)) * a_Y = (price_Y - (B * b_Y)) * a_X
        # price_X * a_Y - (B * b_X * a_Y) = price_Y * a_X - (B * b_Y * a_X)
        # (B * b_Y * a_X) - (B * b_X * a_Y)  = price_Y * a_X - price_X * a_Y 
        # B* ((b_Y * a_X) - (b_X * a_Y))  = price_Y * a_X - price_X * a_Y 
        # B = (price_Y * a_X - price_X * a_Y) / ((b_Y * a_X) - (b_X * a_Y))

        a_X,a_Y = clawmachine.button_a_offset.real,clawmachine.button_a_offset.imag
        b_X,b_Y = clawmachine.button_b_offset.real,clawmachine.button_b_offset.imag
        price_X,price_Y = clawmachine.price_coord.real,clawmachine.price_coord.imag

        B = (price_Y * a_X - price_X * a_Y) / ((b_Y * a_X) - (b_X * a_Y))  
        A = (price_X - (B * b_X)) / a_X

        if A == int(A) and B == int(B):
            clawmachine.cheapest_win = (int(A),int(B),3*int(A)+int(B))
    
    return 
    

f = open("input13.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')