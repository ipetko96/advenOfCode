import re

boards = []

with open('2021\\day04\\input', 'r') as file:
    drawNumbers = [int(number) for number in file.readline().split(',')]
    board = []
    for line in file:
        if line == '\n':
            if len(board) == 0:
                continue
            boards.append(board)
            board = []
            continue
        board.append(list(re.split(r'\s+', line.strip())))
    boards.append(board)


def checkBoard(board):
    rotated = list(zip(*board[::-1]))
    for line in board:
        if checkLine(line):
            return True
    for line in rotated:
        if checkLine(line):
            return True
    return False


def checkLine(line):
    if ''.join(line) == 'xxxxx':
        return True
    else:
        return False


def countBoard(board):
    for i in range(len(board)):
        board[i] = list(filter(('x').__ne__, board[i]))
    clean = [list(map(int, i)) for i in board]
    return sum(sum(clean, []))


for number in drawNumbers:
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if str(number) == boards[i][j][k]:
                    boards[i][j][k] = 'x'
    for l in range(len(boards) - 1, -1, -1):
        if checkBoard(boards[l]):
            if len(boards) == 1:
                print(countBoard(boards[i]) * number)
                break
            else:
                del boards[l]
