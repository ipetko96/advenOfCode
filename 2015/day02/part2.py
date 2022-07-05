import copy

ribbonSum = 0

with open("2015\day02\input", "r") as file:
    for line in file:
        data = line.strip().split("x")
        data = list(map(int, data))
        withoutLength = copy.deepcopy(data)
        withoutLength.pop(withoutLength.index(max(withoutLength)))
        ribbonSum += (2 * withoutLength[0] + 2 * withoutLength[1]) + data[0] * data[1] * data[2]
print(ribbonSum)
