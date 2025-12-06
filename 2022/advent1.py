

def read_input():
    elfs = [0]
    with open("input.txt", "r") as f:
        for line in f:
            line = line[:-1]
            if line == "":
                elfs.append(0)
            else:
                elfs.append(elfs.pop()+int(line))
    return elfs


elf_load = read_input()
print ("Max Load: " + str(max(elf_load)))
elf_load.sort()
print ("Load of Top 3 Elfs: " + str(sum(elf_load[-3:])))