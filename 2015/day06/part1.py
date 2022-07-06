import re

readLinePattern = "([\w\s]+)\s(\d+),(\d+)\s\w+\s(\d+),(\d+)"

lightArray = [[0] * 1000 for _ in range(1000)]


def changeLights(instructions) -> None:
    for i in range(int(instructions.group(2)), int(instructions.group(4)) + 1):
        for j in range(int(instructions.group(3)), int(instructions.group(5)) + 1):
            if "on" in instructions.group(1):
                lightArray[i][j] = 1
            elif "off" in instructions.group(1):
                lightArray[i][j] = 0
            else:
                if lightArray[i][j] == 0:
                    lightArray[i][j] = 1
                else:
                    lightArray[i][j] = 0
    return


with open("2015\day06\input", "r") as file:
    for line in file:
        match = re.match(readLinePattern, line.strip())
        changeLights(match)
    print(sum(x.count(1) for x in lightArray))
