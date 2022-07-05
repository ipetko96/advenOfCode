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
    if diagonal(suradnice):
        if suradnice[0] > suradnice[2] and suradnice[1] > suradnice[3]:
            x1 = suradnice[0]
            y1 = suradnice[1]
            x2 = suradnice[2]
            y2 = suradnice[3]
            while x2 != x1 + 1 and y2 != y1 + 1:
                pole[y2][x2] += 1
                x2 += 1
                y2 += 1
            return
        elif suradnice[0] > suradnice[2] and suradnice[1] < suradnice[3]:
            x1 = suradnice[0]
            y1 = suradnice[1]
            x2 = suradnice[2]
            y2 = suradnice[3]
            while x1 != x2 - 1 and y1 != y2 + 1:
                pole[y1][x1] += 1
                x1 -= 1
                y1 += 1
            return
        elif suradnice[0] < suradnice[2] and suradnice[1] < suradnice[3]:
            x1 = suradnice[0]
            y1 = suradnice[1]
            x2 = suradnice[2]
            y2 = suradnice[3]
            while x1 != x2 + 1 and y1 != y2 + 1:
                pole[y1][x1] += 1
                x1 += 1
                y1 += 1
            return
        elif suradnice[0] < suradnice[2] and suradnice[1] > suradnice[3]:
            x1 = suradnice[0]
            y1 = suradnice[1]
            x2 = suradnice[2]
            y2 = suradnice[3]
            while x1 != x2 + 1 and y1 != y2 - 1:
                pole[y1][x1] += 1
                x1 += 1
                y1 -= 1
            return

    if suradnice[0] >= suradnice[2]:
        x1 = suradnice[0]
        x2 = suradnice[2]
    else:
        x2 = suradnice[0]
        x1 = suradnice[2]
    if suradnice[1] <= suradnice[3]:
        y1 = suradnice[1]
        y2 = suradnice[3]
    else:
        y2 = suradnice[1]
        y1 = suradnice[3]
    if x1 == x2:
        for y in range(y1, y2 + 1):
            pole[y][x1] += 1
        return
    elif y1 == y2:
        for x in range(x2, x1 + 1):
            pole[y1][x] += 1
        return


def getMax(pole):
    return max(map(max, pole))


def countMax(pole):
    sucet = 0
    for i in range(2, getMax(pole) + 1):
        sucet += sum(x.count(i) for x in pole)
    return sucet


for XYbody in suradnice:
    markLine(pole, XYbody)
print(countMax(pole))
