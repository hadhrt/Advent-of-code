import timeit

def p1(lines):
    values = 0
    # get ordering rules and page lists from input 
    ordering_end_index = lines.index("")
    ordering_rules = [tuple(map(int,line.split("|"))) for line in lines[:ordering_end_index]]
    page_lists = [list(map(int,page_list.split(","))) for page_list in lines[ordering_end_index+1:]]
    
    # check each page list against all ordering rules
    valid_page_lists = []
    for page_list in page_lists:
        if is_valid(page_list,ordering_rules): valid_page_lists.append(page_list)

    # sum all middle values of valid lists
    values = sum([page_list[int(len(page_list) / 2)] for page_list in valid_page_lists])
    return values


def p2(lines):
    values = 0
    # get ordering rules and page lists from input 
    ordering_end_index = lines.index("")
    ordering_rules = [tuple(map(int,line.split("|"))) for line in lines[:ordering_end_index]]
    page_lists = [list(map(int,page_list.split(","))) for page_list in lines[ordering_end_index+1:]]
    invalid_page_lists = []

    # check each page list against all ordering rules
    for page_list in page_lists:
        if not is_valid(page_list,ordering_rules): invalid_page_lists.append(page_list)

    corrected_page_lists = [] 
    for page_list in invalid_page_lists:
        # swap values for each ordering rule that is not followed
        while not is_valid(page_list,ordering_rules):
            for (before,after) in ordering_rules:
                if before in page_list and after in page_list:
                    i_after = page_list.index(after)
                    i_before = page_list.index(before)
                    if i_after < i_before:
                        temp = page_list[i_after]
                        page_list[i_after] = page_list[i_before]
                        page_list[i_before] = temp
                        break
        corrected_page_lists.append(page_list)    
    
    # sum all middle values of corrected lists
    values = sum([page_list[int(len(page_list) / 2)] for page_list in corrected_page_lists])                    
    return values


def is_valid (page_list, ordering_rules):
    for (before,after) in ordering_rules:
        if before in page_list and after in page_list:
            if page_list.index(after) < page_list.index(before):
               return False
    return True
    


f = open("input5.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')