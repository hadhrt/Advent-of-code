import math
import timeit
import itertools

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



def p1(lines):
    #init
    values = 0
    num_valves = len(lines)
    dm = [[math.inf for i in range(num_valves)] for j in range(num_valves)]
    ids = []
    valves = []
    END_TIME = 30
    
    
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
    
    #print(str([(ids[x],fr) for (x,fr) in valves]))
       
    
    #starting state
    starting_visited = tuple([ids.index("AA")])
    starting_state = (ids.index("AA"),0,0,0,starting_visited)
    state_stack = [starting_state]
    
    best_state = (starting_state,0)
    max_pressure_from_valve_set = {}
    
   
    while state_stack:
        
        #get state
        state = state_stack.pop()
        
        time_left = END_TIME-state[CURRENT_TIME]
        steam_at_end = state[CURRENT_STEAM] + state[CURRENT_STEAM_RATE] * time_left

        #if all valves are open, finish state
        if len(state[VISITED_VALVES]) == len(valves) + 1:
            if steam_at_end > best_state[MAX_STEAM]:
                best_state = (state,steam_at_end)
            continue
        
        for valve in valves:
            # skip visited opened valves
            if valve[INDEX] in state[VISITED_VALVES]: 
                continue
            #new state when valve is reached and opened
            distance_to_destination = dm[state[CURRENT_VALVE]][valve[INDEX]]            
            time_at_destination = state[CURRENT_TIME] + distance_to_destination + 1
            
            #skip if time would run out and update best state if this is it
            if time_at_destination >= END_TIME:
                if steam_at_end > best_state[MAX_STEAM]:
                    best_state = (state,steam_at_end)
                continue
            
            #create new state for next valve to visit
            steam_at_destination = state[CURRENT_STEAM] + state[CURRENT_STEAM_RATE] * (distance_to_destination + 1)
            steam_rate_at_destination = state[CURRENT_STEAM_RATE] + valve[FLOW_RATE]
            visited_at_destination = state[VISITED_VALVES] + tuple([valve[INDEX]])
            new_state = (valve[INDEX],time_at_destination,steam_at_destination,steam_rate_at_destination, visited_at_destination)
            state_stack.append(new_state)
           
    #s = str([ids[x] for x in best_state[0][VISITED_VALVES]])   
    #print(f"{s}, now at {ids[best_state[0][CURRENT_VALVE]]} at t = {best_state[0][CURRENT_TIME]} and {best_state[0][CURRENT_STEAM]} pressure with {best_state[0][CURRENT_STEAM_RATE]} pressure rate. Will release {best_state[1]} pressure in the end")
    return best_state[1]


    
    
    
def p2(lines):

    #init
    values = 0
    num_valves = len(lines)
    dm = [[math.inf for i in range(num_valves)] for j in range(num_valves)]
    ids = []
    valves = []
    END_TIME = 26
    
    
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
    starting_visited = tuple()
    starting_state = (ids.index("AA"),0,0,0,starting_visited)
    state_stack = [starting_state]
    
    max_pressure_from_valve_set = {}
    
   
    while state_stack:
        
        #get state
        state = state_stack.pop()
        
        time_left = END_TIME-state[CURRENT_TIME]
        steam_at_end = state[CURRENT_STEAM] + state[CURRENT_STEAM_RATE] * time_left
        if steam_at_end > max_pressure_from_valve_set.get(frozenset(state[VISITED_VALVES]),0):
            max_pressure_from_valve_set[frozenset(state[VISITED_VALVES])] = steam_at_end
        
        
        
        #if all valves are open, finish state
        if len(state[VISITED_VALVES]) == len(valves) + 1:
            continue
        
        for valve in valves:
            # skip visited opened valves
            if valve[INDEX] in state[VISITED_VALVES]: 
                continue
            #new state when valve is reached and opened
            distance_to_destination = dm[state[CURRENT_VALVE]][valve[INDEX]]            
            time_at_destination = state[CURRENT_TIME] + distance_to_destination + 1
            
            #skip if time would run out and update best state if this is it
            if time_at_destination >= END_TIME:
                continue
            
            #create new state for next valve to visit
            steam_at_destination = state[CURRENT_STEAM] + state[CURRENT_STEAM_RATE] * (distance_to_destination + 1)
            steam_rate_at_destination = state[CURRENT_STEAM_RATE] + valve[FLOW_RATE]
            visited_at_destination = state[VISITED_VALVES] + tuple([valve[INDEX]])
            new_state = (valve[INDEX],time_at_destination,steam_at_destination,steam_rate_at_destination, visited_at_destination)
            state_stack.append(new_state)
        
    
    max_pressure_from_2_valve_sets = {}
    for p1,p2 in itertools.combinations(max_pressure_from_valve_set.keys(),2):
        if p1.isdisjoint(p2):
            max_pressure_from_2_valve_sets[(p1,p2)] = max_pressure_from_valve_set.get(p1)+max_pressure_from_valve_set.get(p2)
    
    return max_pressure_from_2_valve_sets.get(max(max_pressure_from_2_valve_sets, key=max_pressure_from_2_valve_sets.get))

    

f = open("input16.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print('Time: ', stop - start)