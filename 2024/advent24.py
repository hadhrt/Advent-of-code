import timeit
from collections import deque
import re

def p1(lines):
    initial_values, operations = lines[:lines.index("")], lines[lines.index("")+1:]
    wires = {}
    for line in initial_values:
        wire, val = line.split(": ")
        wires[wire] = int(val)

    
    operation_queue = deque(operations)
    while operation_queue:
        operation = operation_queue.popleft()
        op_match = re.search("(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})", operation)
        wire_in_1, gate, wire_in_2, wire_out = op_match.group(1,2,3,4)
        if wire_in_1 not in wires or wire_in_2 not in wires:
            operation_queue.append(operation)
        else:
            wires[wire_out] = GATES[gate](wires[wire_in_1], wires[wire_in_2])
    

    return int("".join([str(val) for wire,val in sorted(wires.items(),reverse = True) if wire.startswith("z")]),2)


       
def f_AND(x, y):
    return x & y
def f_OR(x, y):
    return x | y
def f_XOR(x, y):
    return x ^ y
GATES = {"AND":f_AND,
       "OR": f_OR,
       "XOR":f_XOR}

GATE_SYMBOL = {"AND":"&",
       "OR": "|",
       "XOR":"^"}

def p2(lines):

    initial_values, operations = lines[:lines.index("")], lines[lines.index("")+1:]
    wires = {}
    for operation in operations:
        wire, val = operation.split(": ")
        wires[wire] = int(val)


    '''
    # sort wires
    for idx,operation in enumerate(operations):
        op, wire_out = operation.split(" -> ")
        wire_in_1, gate, wire_in_2  = op.split(" ")
        if wire_in_2 < wire_in_1:
            operations[idx] = f"{wire_in_2} {gate} {wire_in_1} -> {wire_out}"
    
    subs = {}
    # create substitutions
    for operation in operations:
        op, wire_out = operation.split(" -> ")
        wire_in_1, gate, wire_in_2  = op.split(" ")
        if wire_in_1.startswith("x"):
            if gate == "XOR":
                subs[wire_out] =  f"_presum{wire_in_1[-2:]}"
            elif gate == "AND":
                subs[wire_out] =  f"_precarry{wire_in_1[-2:]}"
                
    #substitute
    for idx,operation in enumerate(operations):
        for sub_from, sub_to in subs.items():
            operation = operation.replace(sub_from, sub_to)
        operations[idx] = operation


    # sort wires
    for idx,operation in enumerate(operations):
        op, wire_out = operation.split(" -> ")
        wire_in_1, gate, wire_in_2  = op.split(" ")
        if wire_in_2 < wire_in_1:
            operations[idx] = f"{wire_in_2} {gate} {wire_in_1} -> {wire_out}"


    for i in range(45):
        for operation in operations:
            op, wire_out = operation.split(" -> ")
            wire_in_1, gate, wire_in_2  = op.split(" ")
            if wire_out.startswith("z") and gate =="XOR":
                if wire_in_1.startswith("_presum"):
                    subs[wire_in_2] =  f"_carry{int(wire_in_1[-2:])-1:02}"

    #substitute
    for idx,operation in enumerate(operations):
        for sub_from, sub_to in subs.items():
            operation = operation.replace(sub_from, sub_to)
        operations[idx] = operation

    # sort wires
    for idx,operation in enumerate(operations):
        op, wire_out = operation.split(" -> ")
        wire_in_1, gate, wire_in_2  = op.split(" ")
        if wire_in_2 < wire_in_1:
            operations[idx] = f"{wire_in_2} {gate} {wire_in_1} -> {wire_out}"


    for i in range(45):
        for operation in operations:
            op, wire_out = operation.split(" -> ")
            wire_in_1, gate, wire_in_2  = op.split(" ")
            if wire_out.startswith("_carry") and gate =="OR":
                if wire_in_1.startswith("_precarry"):
                    subs[wire_in_2] =  f"_procarry{int(wire_in_1[-2:])-1:02}"

    #substitute
    for idx,operation in enumerate(operations):
        for sub_from, sub_to in subs.items():
            operation = operation.replace(sub_from, sub_to)
        operations[idx] = operation

    # sort wires
    for idx,operation in enumerate(operations):
        op, wire_out = operation.split(" -> ")
        wire_in_1, gate, wire_in_2  = op.split(" ")
        if wire_in_2 < wire_in_1:
            operations[idx] = f"{wire_in_2} {gate} {wire_in_1} -> {wire_out}"

    '''

    print("".join(a+"\n" for a in sorted(operations)))

    return 
    

f = open("input24.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')