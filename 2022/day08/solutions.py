with open("2022\\day08\\input", "r") as file:
    stromy = [line.strip() for line in file]


def check_visibility(x: int, y: int) -> bool:
    strany = [stromy[x][y + 1:], "".join([row[y] for row in stromy][x + 1:]), stromy[x][:y], "".join([row[y] for row in stromy][:x])]
    return [True for i in strany if int(stromy[x][y]) > int(max(i))]


count = 0
for i in range(1, len(stromy) - 1):
    for j in range(1, len(stromy[i]) - 1):
        if check_visibility(i, j):
            count += 1

# part 1
print((2 * len(stromy) + 2 * (len(stromy[0]) - 2)) + count)
