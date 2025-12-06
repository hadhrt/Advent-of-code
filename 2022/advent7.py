from collections import deque

def read(lines):
    dirs = {"/":0}
    dir_cur = deque("/")
    for line in lines[1:]:
        cmd = line.split()
        if cmd[0] == "$":
            if cmd[1] == "cd":  
                if cmd[2] == "..":
                    #remove current dir from active dirs
                    dir_cur.pop()
                else:
                    #add current dir to list of dirs and to active dirs
                    dir_cur.append(dir_cur[-1] + "\\" + cmd[2])
                    if cmd[2] not in dirs:
                        dirs[dir_cur[-1]] = 0   
            elif cmd[1] == "ls":
                pass
        #add size to all currently active dirs
        elif cmd[0].isdigit():
            for dir in dir_cur:
                dirs[dir] += int(cmd[0])
    return dirs

def p1(dirs):
    values = sum([size for size in dirs.values() if size < 100000])
    return values


def p2(dirs):
    folder_list = list(dirs.items())
    folder_list.sort(key = lambda x:x[1])
    space_to_free = 30000000 - (70000000 - folder_list[-1][1])
    return [i for i in folder_list if i[1] > space_to_free][0][1]
    

f = open("input7.txt", "r")
lines = [line.strip() for line in f]
dirs = read(lines)


print ("Part 1: " + str(p1(dirs)) )
print ("Part 2: " + str(p2(dirs)) )