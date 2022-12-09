with open("2022\\day08\\tinput", "r") as file:
    stromy = [line.strip() for line in file]


def check_visibility(x: int, y: int) -> bool:
    strany = [stromy[x][y + 1:], "".join([row[y] for row in stromy][x + 1:]), stromy[x][:y], "".join([row[y] for row in stromy][:x])]
    return [True for i in strany if int(stromy[x][y]) > int(max(i))]


def check_cover(x: int, y: int) -> bool:
    score = 1
    strany = [stromy[x][y + 1:], "".join([row[y] for row in stromy][x + 1:]), stromy[x][:y], "".join([row[y] for row in stromy][:x])]
    for i in strany:
        count = 1
        j=0
        while int(stromy[x][y]) > int(i[j]):
            count += 1
            j+=1
        score *= count
    print()

    # doprava = len([i for i in stromy[x][y + 1:] if i < stromy[x][y]])
    # dole = len([i for i in "".join([row[y] for row in stromy][x + 1:]) if i < stromy[x][y]])
    # dolava = len([i for i in stromy[x][:y] if i < stromy[x][y]])
    # hore = len([i for i in "".join([row[y] for row in stromy][:x]) if i < stromy[x][y]])
    
    
    return


count = 0
for i in range(1, len(stromy) - 1):
    for j in range(1, len(stromy[i]) - 1):
        if check_visibility(i, j):
            count += 1

# part 1
print((2 * len(stromy) + 2 * (len(stromy[0]) - 2)) + count)
check_cover(3, 2)
