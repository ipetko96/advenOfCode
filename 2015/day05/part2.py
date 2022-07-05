niceCount = 0


def doubleCharPatternCheck(input: str):
    for i in range(len(input) - 2):
        pattern = input[i : i + 2]
        if line.count(pattern) >= 2:
            return True
    return False


def repeatCheck(input: str):
    for i in range(len(input) - 2):
        pattern = input[i : i + 2] + input[i]
        if pattern in line:
            return True
    return False


with open("2015\day05\input", "r") as file:
    for line in file:
        if doubleCharPatternCheck(line) and repeatCheck(line):
            niceCount += 1
    print(niceCount)
