

def read_input():
    inputlist=[]
    with open("input2.txt", "r") as f:
        for line in f:
            inputlist.append(line[:-1])

    return inputlist



move_dict_part_1 = {
    "A X": 3+1, "B X": 0+1, "C X": 6+1,
    "A Y": 6+2, "B Y": 3+2, "C Y": 0+2,
    "A Z": 0+3, "B Z": 6+3, "C Z": 3+3}
    
move_dict_part_2 = {
    "A X": 0+3, "B X": 0+1, "C X": 0+2,
    "A Y": 3+1, "B Y": 3+2, "C Y": 3+3,
    "A Z": 6+2, "B Z": 6+3, "C Z": 6+1}
    
move_list = read_input()
score_part_1 = 0
score_part_2 = 0
for move in move_list:
    score_part_1 += move_dict_part_1[move]
    score_part_2 += move_dict_part_2[move]
    
    
print("Score Part 1: " + str(score_part_1))

print("Score Part 2: " + str(score_part_2))