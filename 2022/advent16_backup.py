import math

#state indices
CURRENT_VALVE  = 0
CURRENT_TIME   = 1
CURRENT_STEAM  = 2
CURRENT_STEAM_RATE = 3
VISITED_VALVES = 4

#valve indices
INDEX = 0
FLOW_RATE = 1  

#saved state indices
STATE = 0
MAX_STEAM = 1

END_TIME = 30

def p1(lines):
    #init
    values = 0
    num_valves = len(lines)
    dm = [[math.inf for i in range(num_valves)] for j in range(num_valves)]
    ids = []
    valves = []
    
    
    
    #read all valve names
    for line in lines:
        ids.append(line[6:8])
    
    #populate distance matrix
    for idx,line in enumerate(lines):
        dm[idx][idx] = 0
        line = line.split("valve")[1]
        for valve_name in line.split(","):
            neighbour_idx = ids.index(valve_name[1:].strip())
            dm[idx][neighbour_idx] = 1
    
    #find shortest paths in dm
    for k in range(num_valves):
        for i in range(num_valves):
            for j in range(num_valves):
                if dm[i][j] > dm[i][k] + dm[k][j]:
                    dm[i][j] = dm[i][k] + dm[k][j]
    
    
    
    #find all unbroken valves
    for idx,line in enumerate(lines):
        flow_rate = int(line.split(";")[0][23:])
        if flow_rate > 0:
            valves.append((idx,flow_rate))
        
    
    #starting state
    starting_visited = [0]*(len(lines))
    starting_visited[ids.index("AA")] = 1
    starting_state = (0,0,0,0,tuple(starting_visited))
    state_stack = {starting_state}
    checked_states = set()
    best_state = (starting_state,0)
    
    while state_stack:
        
        #get state
        state = state_stack.pop()
        checked_states.add(state)

        time_left = END_TIME-state[CURRENT_TIME]
        steam_at_end = state[CURRENT_STEAM] + state[CURRENT_STEAM_RATE] * time_left
        
        print(f"{state} will release {steam_at_end} pressure")
        #if all valves are open, finish state
        if sum(state[VISITED_VALVES]) == len(valves):
            if steam_at_end > best_state[MAX_STEAM]:
                best_state = (state,steam_at_end)
            continue
        for valve in valves:
            # skip visited opened valves
            if state[VISITED_VALVES][valve[INDEX]] == 1: continue
            #new state when valve is reached and opened
            distance_to_destination = dm[state[CURRENT_VALVE]][valve[INDEX]]            
            time_at_destination = state[CURRENT_TIME] + distance_to_destination + 1
            
            #skip if time would run out and update best state if this is it
            if time_at_destination >= END_TIME: 
                if steam_at_end > best_state[MAX_STEAM]:
                    best_state = (state,steam_at_end)
                continue
            
            steam_at_destination = state[CURRENT_STEAM] + state[CURRENT_STEAM_RATE] * (distance_to_destination + 1)
            
            steam_rate_at_destination = state[CURRENT_STEAM_RATE] + valve[FLOW_RATE]
            visited_at_destination = list(state[VISITED_VALVES])
            visited_at_destination[valve[INDEX]] = 1
            visited_at_destination = tuple(visited_at_destination)
            new_state = (valve[INDEX],time_at_destination,steam_at_destination,steam_rate_at_destination, visited_at_destination)
            
            
            
            if new_state not in state_stack and new_state not in checked_states:
                print(f"going to {ids[valve[INDEX]]}")
                state_stack.add(new_state)
        
        
        
    return best_state


def p2(lines):
    values = 0
    for line in lines:
        pass
    return values
    

f = open("input.txt", "r")
lines = [line.strip() for line in f]
  

print (f"Part 1: {p1(lines)}")
print (f"Part 2: {p2(lines)}")