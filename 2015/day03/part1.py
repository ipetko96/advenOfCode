with open("2015\day03\input", "r") as data:
    instructions = data.read().rstrip()

houses = set()
houses.add((0, 0))

lastPosition = (0, 0)
for direction in instructions:
    actualPosition = list(lastPosition)
    if direction == "^":
        actualPosition[1] += 1
    elif direction == "v":
        actualPosition[1] -= 1
    elif direction == ">":
        actualPosition[0] += 1
    elif direction == "<":
        actualPosition[0] -= 1
    lastPosition = tuple(actualPosition)
    houses.add(lastPosition)
print(len(houses))
