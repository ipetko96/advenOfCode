import re

suradnice, pole = [], []

with open('2021\\day05\\input', 'r') as file:
    for line in file:
        suradnice.append(list(map(int, re.split(r'\,|\s\-\>\s', line))))
    pole = [[0] * (max(map(max, suradnice)) + 1)
            for _ in range(max(map(max, suradnice)) + 1)]


def diagonal(suradnice):
    if suradnice[0] == suradnice[2] or suradnice[1] == suradnice[3]:
        return False
    else:
        return True


def markLine(pole, suradnice):
    if suradnice[0] >= suradnice[2]:
        x1 = suradnice[2]
        x2 = suradnice[0]
    else:
        x1 = suradnice[0]
        x2 = suradnice[2]
    if suradnice[1] >= suradnice[3]:
        y1 = suradnice[3]
        y2 = suradnice[1]
    else:
        y1 = suradnice[1]
        y2 = suradnice[3]
    if x1 == x2:
        for y in range(y1, y2 + 1):
            pole[y][x1] += 1
    else:
        for x in range(x1, x2 + 1):
            pole[y1][x] += 1


def getMax(pole):
    return max(map(max, pole))


def countMax(pole):
    sucet = 0
    for i in range(2, getMax(pole) + 1):
        sucet += sum(x.count(i) for x in pole)
    return sucet


for XYbody in suradnice:
    if not diagonal(XYbody):
        markLine(pole, XYbody)
print(countMax(pole))
