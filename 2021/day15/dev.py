board=[]
with open("2021/day15/tinput", "r") as file:
    for line in file:
        board.append(list(line.strip()))

for i in range(len(board)):
    size=len(board[i])
    for k in range(4):
        for j in range(size):
            board[i].append(board[i][j+k*len(board)]%9+1)

for i in range(len(board)*4):
    board.append([k%9+1 for k in board[i]])

print(board)
