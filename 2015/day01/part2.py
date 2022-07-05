with open("day01\input", "r") as file:
    data = file.read().rstrip()

floor = 0

i = 0
while floor != -1:
    if data[i] == "(":
        floor += 1
    else:
        floor -= 1
    i += 1
print(i)
