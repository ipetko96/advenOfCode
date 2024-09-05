from part1 import get_neighbors

board = []
table = {}
unvisited = []
bigNumber = 999

with open("2021/day15/tinput", "r") as file:
    for line in file:
        board.append(list(line.strip()))

for y in range(5):
    for _ in range(4):
        if board[y][-1] == 9:
            board[y].append(1)
        else:
            board[y].append(board[y][-1]+1)
    if len(board)+1==6:
        break
    if board[y][0] == 9:
        board.append([1])
    else:
        board.append([board[y][0]+1])

for i in range(len(board)):
    for j, value in enumerate(board[i]):
        if i == 0 and j == 0:
            table.update({(i, j): [int(board[i][j]), 0, None]})
        else:
            table.update({(i, j): [int(board[i][j]), bigNumber, None]})
        unvisited.append((i, j))
