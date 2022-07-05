with open("day01\input", "r") as file:
    data = file.read().rstrip()

floor = 0

for char in data:
    if char == "(":
        floor += 1
    else:
        floor -= 1
print(floor)
