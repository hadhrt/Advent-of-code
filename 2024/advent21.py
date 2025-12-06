import timeit
from functools import cache
from itertools import product, pairwise
from collections import Counter 

class DirectionalKeyboard():
    '''
    sequences= {
        "AA": {"A"},          "A^": {"<A"},  "Av": {"<vA", "v<A"},  "A<": {"<v<A","v<<A"},     "A>": {"vA"}, 
        "^A": {">A"},         "^^": {"A"},   "^v": {"vA"},          "^<": {"v<A"},             "^>": {"v>A",">vA"} }
    '''
    buttons = {                   "^": complex(0,1), "A": complex(0,2),
               "<": complex(1,0), "v": complex(1,1), ">": complex(1,2)}

    reverse_buttons = {                    complex(0,1): "^", complex(0,2): "A",
                        complex(1,0): "<", complex(1,1): "v", complex(1,2): ">"}
    
    @cache
    def get_shortest_button_paths(from_pos, to_pos, current_sequence):
        if from_pos == to_pos:
            return set([current_sequence])
        paths = set()
        # ^
        if to_pos.real < from_pos.real:
            next_from_pos = complex(from_pos.real - 1, from_pos.imag )
            if next_from_pos in DirectionalKeyboard.reverse_buttons:
                paths.update(DirectionalKeyboard.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + "^"))
        # v
        if to_pos.real > from_pos.real:
            next_from_pos = complex(from_pos.real + 1, from_pos.imag )
            if next_from_pos in DirectionalKeyboard.reverse_buttons:
                paths.update(DirectionalKeyboard.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + "v"))
        # <
        if to_pos.imag < from_pos.imag:
            next_from_pos = complex(from_pos.real, from_pos.imag - 1 )
            if next_from_pos in DirectionalKeyboard.reverse_buttons:
                paths.update(DirectionalKeyboard.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + "<"))
        # >
        if to_pos.imag > from_pos.imag:
            next_from_pos = complex(from_pos.real, from_pos.imag + 1 )
            if next_from_pos in DirectionalKeyboard.reverse_buttons:
                paths.update(DirectionalKeyboard.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + ">"))
        return paths
    
    def get_shortest_sequences(code):
        sequences = set([""])
        prev_button = "A"
        for button in code:
            new_sequences = DirectionalKeyboard.get_shortest_button_paths(DirectionalKeyboard.buttons.get(prev_button),DirectionalKeyboard.buttons.get(button),"")
            sequences = [s_prev +s +"A" for s_prev,s in product(sequences,new_sequences)]
            prev_button = button
        return sequences

class NumericKeypad():
    buttons = {"7": complex(0,0), "8": complex(0,1), "9": complex(0,2),
               "4": complex(1,0), "5": complex(1,1), "6": complex(1,2),
               "1": complex(2,0), "2": complex(2,1), "3": complex(2,2),
                                  "0": complex(3,1), "A": complex(3,2)}
    reverse_buttons = { complex(0,0): "7", complex(0,1): "8", complex(0,2): "9",
                        complex(1,0): "4", complex(1,1): "5", complex(1,2): "6",
                        complex(2,0): "1", complex(2,1): "2", complex(2,2): "3",
                                           complex(3,1): "0", complex(3,2): "A"}
    @cache
    def get_shortest_button_paths(from_pos, to_pos, current_sequence):
        if from_pos == to_pos:
            return set([current_sequence])
        paths = set()
        # ^
        if to_pos.real < from_pos.real:
            next_from_pos = complex(from_pos.real - 1, from_pos.imag )
            if next_from_pos in NumericKeypad.reverse_buttons:
                paths.update(NumericKeypad.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + "^"))
        # v
        if to_pos.real > from_pos.real:
            next_from_pos = complex(from_pos.real + 1, from_pos.imag )
            if next_from_pos in NumericKeypad.reverse_buttons:
                paths.update(NumericKeypad.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + "v"))
        # <
        if to_pos.imag < from_pos.imag:
            next_from_pos = complex(from_pos.real, from_pos.imag - 1 )
            if next_from_pos in NumericKeypad.reverse_buttons:
                paths.update(NumericKeypad.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + "<"))
        # >
        if to_pos.imag > from_pos.imag:
            next_from_pos = complex(from_pos.real, from_pos.imag + 1 )
            if next_from_pos in NumericKeypad.reverse_buttons:
                paths.update(NumericKeypad.get_shortest_button_paths(next_from_pos, to_pos, current_sequence + ">"))
        return paths
    

    def get_shortest_sequences(code):
        sequences = set([""])
        prev_button = "A"
        for button in code:
            new_sequences = NumericKeypad.get_shortest_button_paths(NumericKeypad.buttons.get(prev_button),NumericKeypad.buttons.get(button),"")
            sequences = [s_prev +s +"A" for s_prev,s in product(sequences,new_sequences)]
            prev_button = button
        return sequences




def p1(lines):
    values = 0

    code_complexity = []
    for code in lines:
        print(code)
        robot_1_inputs = set()
        robot_2_inputs = set()
        my_inputs =set()
        robot_1_inputs.update(NumericKeypad.get_shortest_sequences(code))
        r1_shortest_s = min([len(i) for i in robot_1_inputs])
        robot_1_inputs =  set( [s for s in robot_1_inputs if len(s) == r1_shortest_s])
        for robot_1_input in robot_1_inputs:
            robot_2_inputs.update(DirectionalKeyboard.get_shortest_sequences(robot_1_input))
            r2_shortest_s = min([len(i) for i in robot_2_inputs])
            robot_2_inputs =  set( [s for s in robot_2_inputs if len(s) == r2_shortest_s])
            for robot_2_input in robot_2_inputs:
                my_inputs.update(DirectionalKeyboard.get_shortest_sequences(robot_2_input))
                my_shortest_s = min([len(i) for i in my_inputs])
                my_inputs =  set( [s for s in my_inputs if len(s) == my_shortest_s])
        code_complexity.append((code, min([len(i) for i in my_inputs]), int(code[:-1])  ))
    
    return sum([a*b for _,a,b in code_complexity])


def get_higher_sequence(sequence):
    new_sequence = ""
    for b1,b2 in pairwise("A"+sequence):
        new_sequence += best_transition_moves.get(b1+b2)
    return new_sequence


def get_higher_sequences(sequence):
    higher_sequences = [""]
    for b1,b2 in pairwise("A"+sequence):
        tms = transition_moves.get(b1+b2)
        next_higher_sequences = []
        for tm in tms:
            next_higher_sequences += [bb + tm for bb in higher_sequences]
        higher_sequences = next_higher_sequences
    return higher_sequences


transition_moves = {'<<': {'A'} ,           '<>': {'>>A'},        '<^': {'>^A'},        '<v': {'>A'},         '<A': {'>^>A', '>>^A'}, 
                    '><': {'<<A'},          '>>': {'A'},          '>^': {'<^A', '^<A'}, '>v': {'<A'},         '>A': {'^A'}, 
                    '^<': {'v<A'},          '^>': {'>vA', 'v>A'}, '^^': {'A'},          '^v': {'vA'},         '^A': {'>A'}, 
                    'v<': {'<A'},           'v>': {'>A'},         'v^': {'^A'},         'vv': {'A'},          'vA': {'^>A', '>^A'}, 
                    'A<': {'<v<A', 'v<<A'}, 'A>': {'vA'},         'A^': {'<A'},         'Av': {'v<A', '<vA'}, 'AA': {'A'}}
best_transition_moves = {
                    '<<': 'A' ,           '<>': '>>A',        '<^': '>^A',        '<v': '>A',         '<A': '>>^A', 
                    '><': '<<A',          '>>': 'A',          '>^': '<^A',        '>v': '<A',         '>A': '^A', 
                    '^<': 'v<A',          '^>': 'v>A',        '^^': 'A',          '^v': 'vA',         '^A': '>A', 
                    'v<': '<A',           'v>': '>A',         'v^': '^A',         'vv': 'A',          'vA': '^>A', 
                    'A<': 'v<<A',         'A>': 'vA',         'A^': '<A',         'Av': '<vA',        'AA': 'A'}

def p2(lines):

    '''
    # find the best transitions:
    for set_a in transition_moves.values():
        if len(set_a) > 1:
            print(f"{set_a}")
            for test_seq in set_a:
                seqs_plus_1 = get_higher_sequences(test_seq)
                seqs_plus_2 = []
                for seq_plus_1 in seqs_plus_1:
                    seqs_plus_2+=get_higher_sequences(seq_plus_1)
                min_seq = min([len(seq) for seq in seqs_plus_2])
                print(f"{test_seq} : {min_seq}")
    '''

    code_complexity = []
    num_robots = 2
    for code in lines:
        poss_codes = NumericKeypad.get_shortest_sequences(code)
        next_seq = get_higher_sequence(poss_codes[0])
        for poss_code in poss_codes:
            if len(get_higher_sequence(poss_code)) < len(next_seq):
                next_seq = get_higher_sequence(poss_code)
        sequence = next_seq

        for i in range(num_robots-1):
            sequence = get_higher_sequence(sequence)

        code_complexity.append((code, len(sequence), int(code[:-1])))




    return sum([a*b for _,a,b in code_complexity])

    

f = open("input.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
#print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')