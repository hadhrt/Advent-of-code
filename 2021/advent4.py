

def p1(f):
    f = open(f_name, "r")
    #read numbers
    numbers = [int(x) for x in f.readline().strip().split(',')]
    
    #read boards
    boards = []
    while True:
        boardline = "".join([f.readline().strip()+" " for i in range(6)])
        if len(boardline) < 25: break
        boards.append(list(map(int,boardline.split())))
    
    #cross out numbers in boards
    value = 0
    for num in numbers:
        for index,board in enumerate(boards):
            board = ['X' if x == num else x for x in board]
            boards[index] = board
            if checkboard(board) == True:
                board = [0 if x == 'X' else x for x in board]
                value = sum(board)*num
                return value
    return 0
    
    
def p2(f_name):
    #read numbers
    f = open(f_name, "r")
    numbers = [int(x) for x in f.readline().strip().split(',')]
    
    #read boards
    boards = []
    while True:
        boardline = "".join([f.readline().strip()+" " for i in range(6)])
        if len(boardline) < 25: break
        boards.append(list(map(int,boardline.split())))
    
    #cross out numbers in boards
    value = 0
    for num in numbers:
        rem = []
        for index,board in enumerate(boards):
            board = ['X' if x == num else x for x in board]
            boards[index] = board

            if checkboard(board) == True:
                if len(boards) == 1:
                    board = [0 if x == 'X' else x for x in board]
                    value = sum(board)*num
                    return value
                rem.append(boards[index])
        for b in rem:
            boards.remove(b)
    return 0    
    

def checkboard(board):
    # row
    for i in range(5):
        if board[5*i:5*i+5].count("X") == 5: return True
    # column
    for i in range(5):
        if [x for x in board[i::5]].count("X") == 5: return True
        
    return False

def printboard(board):
    for i in range(5):
        z =''
        for j in range(5):
            if board[5*i+j]== "X": z += " X "
            else: z += f'{board[5*i+j]:2d} '
        print(z)
    print(checkboard(board))
    
    


f_name = "input4.txt"
#lines = [line.strip() for line in f]
  

print ("Part 1: " + str(p1(f_name)) )
print ("Part 2: " + str(p2(f_name)) )