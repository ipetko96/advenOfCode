with open("2015\day03\input", "r") as data:
    instructions = data.read().rstrip()

moveData = {"santa": {"lastPosition": [0, 0]}, "roboSanta": {"lastPosition": [0, 0]}}
visitedHouses = set()

visitedHouses.add((0, 0))


def move(person: str, direction: str):
    if direction == "^":
        moveData[person]["lastPosition"][1] += 1
    elif direction == "v":
        moveData[person]["lastPosition"][1] -= 1
    elif direction == ">":
        moveData[person]["lastPosition"][0] += 1
    elif direction == "<":
        moveData[person]["lastPosition"][0] -= 1
    visitedHouses.add(tuple(moveData[person]["lastPosition"]))


for i in range(len(instructions)):
    if i % 2 == 0:
        move("santa", instructions[i])
    else:
        move("roboSanta", instructions[i])


print(len(visitedHouses))
