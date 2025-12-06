import timeit
from collections import deque



def p1(lines):
    neighbours = {}

    for line in lines:
        names = line.split('-')

        # create caves if they dont exist yet
        if not neighbours.get(names[0]):          
            neighbours[names[0]] = []
        if not neighbours.get(names[1]):
            neighbours[names[1]] = []
        # add connection
        if names[0] not in neighbours[names[1]]:
            neighbours[names[1]].append(names[0])
        if names[1] not in neighbours[names[0]]:
            neighbours[names[0]].append(names[1])
    finished_states = deque()

    states =  deque([["start"]])

    while states:
            state = states.popleft()
            current_pos =  state[-1]
            for cave in neighbours[current_pos]:
                if cave == "end":
                    finished_states.appendleft(state + [cave])
                    continue
                if cave not in state or cave[0].isupper():
                    states.appendleft(state + [cave])
    #for state in finished_states:
    #    print_state(state)
    return len(finished_states)

def print_state(state):
    str = "".join([cave+"," for cave in state])[:-1]
    print(str)

def p2(lines):

    neighbours = {}

    for line in lines:
        names = line.split('-')

        # create caves if they dont exist yet
        if not neighbours.get(names[0]):          
            neighbours[names[0]] = []
        if not neighbours.get(names[1]):
            neighbours[names[1]] = []
        # add connection
        if names[0] not in neighbours[names[1]]:
            neighbours[names[1]].append(names[0])
        if names[1] not in neighbours[names[0]]:
            neighbours[names[0]].append(names[1])
    finished_states = deque()

    states =  deque([["0","start"]])

    while states:
            state = states.popleft()
            current_pos =  state[-1]
            for cave in neighbours[current_pos]:
                if cave == "end":
                    finished_states.appendleft(state + [cave])
                    continue
                if cave[0].isupper():
                    states.appendleft(state + [cave])
                else:
                    if cave not in state:
                        states.appendleft(state + [cave])
                    elif cave != "start" and cave !="end" and state[0] == "0":
                        states.appendleft(["1"] + state[1:] + [cave])
#    for state in finished_states:
#        print_state(state)
    return len(finished_states)
    

f = open("input12.txt", "r")
lines = [line.strip() for line in f]
  

start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)