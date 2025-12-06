import re
import sys
sys.setrecursionlimit(10**5)

import timeit



ORES = 0
CLAY = 1
OBSIDIAN = 2
GEODES = 3
ORE_ROBOTS = 4
CLAY_ROBOTS = 5
OBSIDIAN_ROBOTS = 6
GEODE_ROBOTS = 7
TIME = 8
FINAL_GEODES = 9


BP_NUMBER = 0
ORE_ROBOT_ORE_COST = 1
CLAY_ROBOT_ORE_COST = 2
OBSIDIAN_ROBOT_ORE_COST = 3
OBSIDIAN_ROBOT_CLAY_COST = 4
GEODE_ROBOT_ORE_COST = 5
GEODE_ROBOT_OBSIDIAN_COST = 6

NO_NEXT_ROBOT = 0
ORE_ROBOT_NEXT = 1
CLAY_ROBOT_NEXT = 2
OBSIDIAN_ROBOT_NEXT = 3
GEODE_ROBOT_NEXT = 4

def p1(lines):
    values = []
    bps = []
    for line in lines:
        costs = list(map(int,re.findall(r'\d+',line)))
        bps.append(costs)


    for bp in bps:
        # start with 1 ore robot and 24 minutes remaining 
        state = [0,0,0,0,1,0,0,0,0,0]
        value = find_best(state,bp,NO_NEXT_ROBOT,24)
        values.append((bp[BP_NUMBER],value))

    
    
    #print(values)  

    return sum([id*val for id, val in values])



def find_best(state,bp,buildnext,max_time):
    
    #print((state,buildnext))
     
    build_ore_robot = build_clay_robot = build_obsidian_robot = build_geode_robot = False
    
    #build ore robot
    if buildnext == ORE_ROBOT_NEXT:
        #can an ore robot be build?
        if bp[ORE_ROBOT_ORE_COST] <= state[ORES]:
            #print("Building Ore Robot")
            state[ORE_ROBOTS] += 1  
            state[ORES] -= bp[ORE_ROBOT_ORE_COST]
            #remove new robots production
            state[ORES] -= 1
            buildnext = NO_NEXT_ROBOT
        else:
            build_ore_robot = True
        
    #build clay robot
    if buildnext == CLAY_ROBOT_NEXT:
        #can a clay robot be build?
        if bp[CLAY_ROBOT_ORE_COST] <= state[ORES]:
            #print("Building Clay Robot")
            state[CLAY_ROBOTS] += 1
            state[ORES] -= bp[CLAY_ROBOT_ORE_COST]
            #remove new robots production
            state[CLAY] -= 1
            buildnext = NO_NEXT_ROBOT
        else:
            build_clay_robot = True
            
    #build obsidian robot
    if buildnext == OBSIDIAN_ROBOT_NEXT:
        #can an obsidian robot be build?
        if bp[OBSIDIAN_ROBOT_ORE_COST] <= state[ORES] and bp[OBSIDIAN_ROBOT_CLAY_COST] <= state[CLAY]:
            #print("Building Obsidian Robot")
            state[OBSIDIAN_ROBOTS] += 1  
            state[ORES] -= bp[OBSIDIAN_ROBOT_ORE_COST]
            state[CLAY] -= bp[OBSIDIAN_ROBOT_CLAY_COST]
            #remove new robots production
            state[OBSIDIAN] -= 1
            buildnext = NO_NEXT_ROBOT
        else:
            build_obsidian_robot = True
            
    #build geode robot
    if buildnext == GEODE_ROBOT_NEXT:
        #can a geode robot be build?
        if bp[GEODE_ROBOT_ORE_COST] <= state[ORES] and bp[GEODE_ROBOT_OBSIDIAN_COST] <= state[OBSIDIAN]:
            #print("Building Geode Robot")
            state[GEODE_ROBOTS] += 1
            state[ORES] -= bp[GEODE_ROBOT_ORE_COST]
            state[OBSIDIAN] -= bp[GEODE_ROBOT_OBSIDIAN_COST]
            #remove new robots production
            state[GEODES] -= 1
            buildnext = NO_NEXT_ROBOT
        else:
            build_geode_robot = True
    
    
    #progress  state
    state[ORES] += state[ORE_ROBOTS]
    state[CLAY] += state[CLAY_ROBOTS]
    state[GEODES] += state[GEODE_ROBOTS]
    state[OBSIDIAN] += state[OBSIDIAN_ROBOTS]
    state[TIME] += 1
    
    #time is up, branch is finished
    if state[TIME] == max_time:
        #print("finished")
        return state[GEODES]
    


    #decide what to do next
    if buildnext == NO_NEXT_ROBOT:
        
        
        build_ore_robot = build_clay_robot = build_obsidian_robot = build_geode_robot = True
        
        
        #should an ore robot be build?
        if state[ORE_ROBOTS] > max(bp[CLAY_ROBOT_ORE_COST], bp[OBSIDIAN_ROBOT_ORE_COST], bp[GEODE_ROBOT_ORE_COST]):
            build_ore_robot =  False
            
        #should a clay robot be build?
        max_obsidian_robots_to_build = 21-state[TIME]
        useful_clay = max_obsidian_robots_to_build * bp[OBSIDIAN_ROBOT_CLAY_COST]
        if state[CLAY] + (21-state[TIME])*state[CLAY_ROBOTS] > useful_clay:
            build_clay_robot =  False
        
        if state[CLAY_ROBOTS] > bp[OBSIDIAN_ROBOT_CLAY_COST]:
            build_clay_robot =  False
            
        #should an obsidian robot be build?
        if state[CLAY_ROBOTS] == 0:
            build_obsidian_robot = False
        
            
        #should a geode robot be build?
        if state[CLAY_ROBOTS] == 0 or state[OBSIDIAN_ROBOTS] == 0:
            build_geode_robot = False
        
        #should any robot be build?
        if state[TIME] > max_time-5:
            build_clay_robot =  False
        if state[TIME] > max_time-3:
            build_ore_robot =  False
            build_clay_robot =  False
            build_obsidian_robot =  False 
        #if a geode robot can be build, build it!    
        if bp[GEODE_ROBOT_ORE_COST] <= state[ORES] and bp[GEODE_ROBOT_OBSIDIAN_COST] <= state[OBSIDIAN]:
            build_ore_robot =  False
            build_clay_robot =  False
            build_obsidian_robot =  False
     

    #call next steps:
        
    result_idle = result_ore = result_clay = result_obsidian = result_geode = 0    
        
    #build ore robot
    if build_ore_robot:
        #print("Build Ore Robot")
        state_ore = state.copy()
        result_ore = find_best(state_ore,bp,ORE_ROBOT_NEXT,max_time)
    #build clay robot
    if build_clay_robot:
        #print("Build Clay Robot")
        state_clay = state.copy()
        result_clay = find_best(state_clay,bp,CLAY_ROBOT_NEXT,max_time)
    #build obsidian robot
    if build_obsidian_robot:
        #print("Build Obsidian Robot")
        state_obsidian = state.copy()
        result_obsidian = find_best(state_obsidian,bp,OBSIDIAN_ROBOT_NEXT,max_time)
    #build geode robot
    if build_geode_robot:
        state_geode = state.copy()
        result_geode = find_best(state_geode,bp,GEODE_ROBOT_NEXT,max_time)

      
    
    return max(result_ore, result_clay, result_obsidian, result_geode)




def p2(lines):
    values = []
    bps = []
    lines = lines[:3]
    for line in lines:
        costs = list(map(int,re.findall(r'\d+',line)))
        bps.append(costs)


    for bp in bps:
        # start with 1 ore robot and 32 minutes remaining 
        state = [0,0,0,0,1,0,0,0,0,0]
        value = find_best(state,bp,NO_NEXT_ROBOT,32)
        values.append(value)


    print(values)
    ret_val = 1
    for val in values:
        ret_val = ret_val * val

    return ret_val
    

f = open("input19.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()

print('Time: ', stop - start) 

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()

print('Time: ', stop - start)