from re import findall

regexPattern = r"1+|2+|3+|4+|5+|6+|7+|8+|9+"

with open("2015//day10//input") as file:
    data = file.read().strip()


def encodeString(input: str) -> str:
    parsed = findall(regexPattern, input)
    for i in range(len(parsed)):
        parsed[i] = str(len(parsed[i])) + str(parsed[i][0])
    return "".join(parsed)


for _ in range(50):
    data = encodeString(data)

print(len(data))
