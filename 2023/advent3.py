import timeit
import re

def p1(lines):
    values = 0
    symbols = set()
    #find all symbol types
    for line in lines:
        for char in line:
            symbols.add(char)
    symbols = symbols - set(("0","1","2","3","4","5","6","7","8","9","."))
    
    numbers = []

    #find all numbers
    for line_idx,line in enumerate(lines):
        for match in re.finditer("\d+",line):
            search_start = max(match.start()-1,0)
            search_end = min(match.end()+1,len(line))
            #find all adjecent symbols
            adj_symbols = set()
            if line_idx>=1: 
                [adj_symbols.add(char) for char in lines[line_idx-1][search_start:search_end]]
            [adj_symbols.add(char) for char in lines[line_idx][search_start:search_end]]
            if line_idx+1<len(lines): 
                [adj_symbols.add(char) for char in lines[line_idx+1][search_start:search_end]]
            adj_symbols = adj_symbols.intersection(symbols)
            numbers.append((adj_symbols,int(match.group())))

    values = sum([number[1] for number in numbers if number[0] != set()])
    return values


def p2(lines):
    values = 0
    grid = dict()
    # index all numbers
    for row,line in enumerate(lines):
        for match in re.finditer("\d+",line):
            for col in range(match.start(), match.end()):
                grid[(row,col)] = int(match.group())

    # find all gear symbols
    for row,line in enumerate(lines):
        for col,char in enumerate(line):
            if char == "*":
                #check for numbers in vicinity
                adj_pos = ((row-1,col-1),(row-1,col+0),(row-1,col+1),
                           (row+0,col-1),(row+0,col+0),(row+0,col+1), 
                           (row+1,col-1),(row+1,col+0),(row+1,col+1))
                adj_numbers = list(set([grid.get(pos) for pos in adj_pos]) - set([None]))
                if len(adj_numbers) == 2:
                    values += adj_numbers[0] * adj_numbers[1]
    return values
    

f = open("input3.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')