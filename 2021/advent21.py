import timeit


def p1(lines):
    die_pos = 1
    die_rolls = 0
    p1_score = 0
    p2_score = 0
    p1_pos = int(lines[0][28:])
    p2_pos = int(lines[1][28:])
    turn = 1

    while p1_score < 1000 and p2_score < 1000:
        move = 3*die_pos +3
        die_rolls += 3
        die_pos = (die_pos + 2) %100 +1
        if turn == 1:
            p1_pos = ((p1_pos + move -1 ) % 10)+1
            p1_score += p1_pos
            turn = 2
        elif turn == 2:
            p2_pos = ((p2_pos + move -1 ) % 10)+1
            p2_score += p2_pos
            turn = 1

    return min(p1_score,p2_score)*die_rolls


def p2(lines):
    #state (p1_score, p1_pos, p2_score, p2_pos)
    WINSCORE = 21
    p1_score = 0
    p2_score = 0
    p1_pos = int(lines[0][28:])
    p2_pos = int(lines[1][28:])  

    init_state = (p1_score, p1_pos, p2_score, p2_pos)
    states = {init_state:1}
    turn = 1
    moves =[(3, 1),  (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


    p1_win_universes_count = 0
    p2_win_universes_count = 0

    while states:

        new_states = {}
        for (state_p1_score, state_p1_pos, state_p2_score, state_p2_pos), state_count in states.items():
            for move, move_count in moves:
                if turn == 1:
                    move_p1_pos = ((state_p1_pos + move -1 ) % 10)+1
                    move_p1_score = state_p1_score + move_p1_pos
                    move_p2_pos = state_p2_pos
                    move_p2_score =  state_p2_score
                elif turn == 2:
                    move_p2_pos = ((state_p2_pos + move -1 ) % 10)+1
                    move_p2_score = state_p2_score + move_p2_pos
                    move_p1_pos = state_p1_pos
                    move_p1_score =  state_p1_score
                new_state = (move_p1_score, move_p1_pos, move_p2_score, move_p2_pos)
                
                if move_p1_score >= WINSCORE:
                    #assert(move_p2_score < WINSCORE)
                    p1_win_universes_count += state_count*move_count
                elif move_p2_score >= WINSCORE:
                    #assert(move_p1_score < WINSCORE)
                    p2_win_universes_count += state_count*move_count
                else:
                    #assert(move_p1_score < WINSCORE)
                    #assert(move_p2_score < WINSCORE)
                    new_states[new_state] = new_states.get(new_state ,0) + state_count*move_count
        states = new_states
        turn = turn ^3 

    return max(p1_win_universes_count, p2_win_universes_count)
    

f = open("input21.txt", "r")
lines = [line.strip() for line in f]
  

start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)