niceCount = 0
rules = {"vowels": ["a", "e", "i", "o", "u"], "forbidden": ["ab", "cd", "pq", "xy"]}


def forbiddenCheck(input: str):
    for i in rules["forbidden"]:
        if i in input:
            return False
    return True


def vowelsCount(input: str):
    vowelsCount = 0
    for i in rules["vowels"]:
        if i in input:
            vowelsCount += input.count(i)
        if vowelsCount >= 3:
            return True
    return False


def doubleCharCheck(input: str):
    for i in range(len(input) - 2):
        if input[i] == input[i + 1]:
            return True
    return False


with open("2015\day05\input", "r") as file:
    for line in file:
        if forbiddenCheck(line) and vowelsCount(line) and doubleCharCheck(line):
            niceCount += 1
    print(niceCount)
