import timeit
import math
from bisect import bisect_left

START = 0
END = 1
OFFSET = 2


def p1(lines):
    values = 0
    map_lines = lines.split("\n\n")
    _,seeds = map_lines[0].split(":")
    seeds = list(map(int,seeds.split()))
    map_lines = map_lines[1:]
    # each map in maps contains all conversion values as tuples
    conv_maps = [[] for _ in map_lines]
    for map_idx,map_line in enumerate(map_lines):
        _,map_value_line = map_line.split(":")
        for map_value in map_value_line.strip().split("\n"):
            values = list(map(int,map_value.split()))
            # conversion tuple: (source value, range, destination)
            conv_maps[map_idx].append((values[1],values[2],values[0]))
            pass
        conv_maps[map_idx].sort()
    
    seed_conversions = []
    for seed in seeds:
        seed_conv = [seed]
        for conv_map in conv_maps:
            #find next lowest conv_map value and check if seed is in range
            next_lowest_value_idx = bisect_left(conv_map,(seed_conv[-1],math.inf))
            if next_lowest_value_idx == 0:
                #seed outside of all ranges
                seed_conv.append(seed_conv[-1])
                continue
            conv_tuple = conv_map[next_lowest_value_idx-1]
            seed_to_source_offset = seed_conv[-1] - conv_tuple[0]
            if seed_to_source_offset > conv_tuple[1]:
                #seed outside of all ranges
                seed_conv.append(seed_conv[-1])
            else:
                seed_conv.append(conv_tuple[2] + seed_to_source_offset)
        seed_conversions.append(tuple(seed_conv))            

    values = min([seed_conv[-1] for seed_conv in seed_conversions])
    return values


def p2(lines):
    map_lines = lines.split("\n\n")
    # extract seed ranges:
    _,single_seeds = map_lines[0].split(":")
    single_seeds = list(map(int,single_seeds.split()))
    seeds = [(seed,seed + seed_range - 1) for seed, seed_range in zip(single_seeds[::2],single_seeds[1::2])]

    # remove seed line from input
    map_lines = map_lines[1:]
    # each map in maps contains all conversion values as tuples
    conv_maps = [[] for _ in map_lines]
    for map_idx,map_line in enumerate(map_lines):
        _,map_value_line = map_line.split(":")
        for map_value in map_value_line.strip().split("\n"):
            # values in input: (destination start, source start, range)
            values = list(map(int,map_value.split()))
            # values in conversion tuple: (source start, source end, conversion offset)
            conversion_tuple = (values[1], values[1] + values[2] - 1, values[0] - values[1])
            conv_maps[map_idx].append(conversion_tuple)
        conv_maps[map_idx].sort()

    # take all seed ranges and apply conversion to soil ranges
    # variables named for first conversion from seed to soil, but loop iterates over all conversions
    for soil_map in conv_maps:
        possible_soils = []
        for seed in seeds:
            low_seed_idx = seed[START]

            # loop through all soils and return all overlaps with seed as possible soils
            # v    v        v    v                   v              low_seed_idx value iterations
            # |---------seed_1----------|            |-seed_2-|     seeds
            #      |-soil_1-|    |-soil_2-| |soil_3|                soils
            # |-1.-|----3.--|-1.-|--3.--|      2.    |----4.--|     corrp. loop section and new possible soils
            #
            for soil in soil_map:
            # 1. seed starts before soil
                if low_seed_idx < soil[START]:
                    # seed end before soil start
                    if seed[END] < soil[START]:
                        possible_soils.append((low_seed_idx, seed[END]))
                        low_seed_idx = seed[END] + 1
                        break
                    # process range until soil start
                    else:
                        possible_soils.append((low_seed_idx, soil[START] - 1))
                        low_seed_idx = soil[START]
            # 2. seed starts after soil end:
                if low_seed_idx > soil[END]:
                    continue
            # 3. seed now starts in soil range
                assert(low_seed_idx >= soil[START])
                assert(low_seed_idx <= soil[END])
                # either seed ends:
                if seed[END] <= soil[END]:
                    possible_soils.append((low_seed_idx + soil[OFFSET], seed[END] + soil[OFFSET]))   
                    low_seed_idx = seed[END] + 1
                    break
                # or soil ends:
                possible_soils.append((low_seed_idx + soil[OFFSET], soil[END] + soil[OFFSET]))
                low_seed_idx = soil[END] + 1
                
            # 4. process remaining seed
            if low_seed_idx <= seed[END]:
                possible_soils.append((low_seed_idx, seed[END]))
        seeds = possible_soils
    values = min([seed[0] for seed in seeds])
    return values
    

f = open("input5.txt", "r")
lines = f.read()
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')