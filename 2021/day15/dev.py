board=[[1,2],[3,4]]
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
print(board)