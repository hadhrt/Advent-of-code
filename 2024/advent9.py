import timeit
import heapq

def p1(lines):
    disk = []
    for line in lines:
        file = True
        file_id = 0
        for char in line:
            if file:
                disk.extend(int(char)*[file_id])
                file = False
                file_id += 1
            else:
                disk.extend(int(char)*["."])
                file = True
    #print("".join([str(element) for element in disk]))
    
    while "." in disk:
        index = disk.index(".")
        new_element = disk.pop()
        while new_element == ".": new_element = disk.pop()
        if index < len(disk):
            disk[index] = new_element
    #print("".join([str(element) for element in disk]))

    return sum(index*value for index,value in enumerate(disk))

def p1_nodisk(lines):
    line = lines[0]
    files = []
    spaces = []
    file_next = True
    file_id = 0
    index = 0
    for char in line:
        if file_next:
            file_size = int(char)
            for _ in range(file_size):
                files.append((index,file_id))
                index += 1
            file_next = False
            file_id += 1
           
        else:
            space_size = int(char)
            for _ in range(space_size): 
                heapq.heappush(spaces, index)
                index += 1
            file_next = True
    new_file_list = []
    for file in reversed(files):
        # is a suitabel space remaining?
        if len(spaces) > 0 and spaces[0] < file[0]:
            new_file_list.append((heapq.heappop(spaces), file[1]))
        else:
            new_file_list.append(file)


    return sum(index*file_id for index, file_id in new_file_list)

def p2(lines):
    SPACEREPR = "."
    disk = []
    line = lines[0]
    files = []
    spaces = []
    file = True
    file_id = 0
    for char in line:
        if file:
            index = len(disk)
            disk.extend(int(char)*[file_id])
            files.append((index,int(char),file_id))
            file = False
            file_id += 1
           
        else:
            index = len(disk)
            disk.extend(int(char)*[SPACEREPR])
            spaces.append((index,int(char)))
            file = True
    #print("".join([str(element) for element in disk]))

    for file in reversed(files):
        # search for earlies space big enough
        for index,space in enumerate(spaces):
            if file[1] > space[1]:
                continue
            if file[0] < space[0]:
                continue
            elif file[1] == space[1]:
                spaces.remove(space)
            else:
                newspace = (space[0]+file[1],space[1]-file[1])
                spaces[index] = newspace
            # swap space and file on disk
            for i in range(file[1]):
                disk[space[0]+i] = file[2]
                disk[file[0]+i] = SPACEREPR
            break

    #print("".join([str(element) for element in disk]))

    return sum(index*value for index,value in enumerate(disk) if value != ".")
    

def p2_nodisk(lines):

    line = lines[0]
    files = []
    spaces = [[],[],[],[],[],[],[],[],[],[]]
    file_next = True
    file_id = 0
    index = 0
    for char in line:
        if file_next:
            file_size = int(char)
            files.append((index,file_size,file_id))
            index += file_size
            file_next = False
            file_id += 1
           
        else:
            space_size = int(char)
            heapq.heappush(spaces[space_size], index)
            index += space_size
            file_next = True

    new_file_list = []
    for file in reversed(files):
        
        # find the earliest sufficiently large space
        next_open_space = file[0]
        next_open_space_size = 0
        for size in range(file[1],10):
            if len(spaces[size]) != 0:
                if spaces[size][0] < next_open_space:
                    next_open_space = spaces[size][0]
                    next_open_space_size = size
        
        # if no suitable space is found, go to next file
        if next_open_space_size == 0:
            new_file_list.append(file)
        
        # if a suitable space is found:
        if next_open_space_size > 0:
            # remove the empty space
            space_index = heapq.heappop(spaces[next_open_space_size])
            # create new space is space > file size
            remaining_space = next_open_space_size - file[1]
            if remaining_space > 0:
                new_space_index = space_index + file[1]
                heapq.heappush(spaces[remaining_space],new_space_index)
            # save the file at new location
            new_file_list.append((space_index,file[1],file[2]))
            
    checksum = 0
    for file in new_file_list:
        for i in range(file[1]):
            add = (i+file[0]) * file[2]
            checksum += add
    return checksum


f = open("input9.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
#print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 1(without disk): {p1_nodisk(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
#print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2 (without disk): {p2_nodisk(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')