import timeit
import itertools
import regex as re

class Springs(list):
    def matches (self, clues):
        return clues == [len(group) for group in self.split(".")]


def p1(lines):
    values = 0
    springs = []
    clues = []
    for line in lines:
        springs.append(line.split()[0])
        clues.append(list(map(int,line.split()[1].split(","))))
    possible_springs = []
    for idx, spring in enumerate(springs):
        spring_l = list(spring)
        unknown_idxs = [idx for idx,char in enumerate(spring_l) if char == "?"]
        possible_springs.append([])
        # all combinations of "." and "#"
        for subst in itertools.product([".","#"], repeat = len(unknown_idxs)):
            # substitute all "?"
            for subst_idx,pos in enumerate(unknown_idxs):
                spring_l[pos] = subst[subst_idx]
            # check if substitution matches clues
            poss_str = "".join(spring_l)
            poss_str_clues = [len(group) for group in poss_str.replace("."," ").split()]
            if poss_str_clues == clues[idx]:
                possible_springs[idx].append(poss_str)

    values = sum([len(poss_spr)for poss_spr in possible_springs])

    return values


def get_possibilities(spring_str, conditions):
    possibilities = 0
    # recursion break conditions
    if spring_str < sum(conditions)+len(conditions)-1:
        return 0

    group_len = conditions[0]
    # find all groups of # or ? with length of group, followed by . or end of str
    re_pattern = "[\?#]{"+ str(group_len) + "}([\?\.]|$)"
    # for each match, process the remaining string and conditions and add the possibilities
    for re_match in re.finditer(re_pattern, spring_str, overlapped = True):
        remaining_str = spring_str[re_match.end():]
        remaining_conditions = conditions[1:]
        possibilities += get_possibilities(remaining_str, remaining_conditions)
    return possibilities





def p2(lines):
    values = 0
    a = ".??..??...?##"
    cond = [2,3]
    get_possibilities(a,cond)
    for line in lines:
        pass
    return values
    

f = open("input12.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
#print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')