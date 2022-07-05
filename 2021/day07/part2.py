with open('2021\\day07\\tinput', 'r') as file:
    crabs = [int(number) for number in file.readline().split(',')]

fuel = []
for j in range(len(crabs)):
    lineup = 0
    for i in crabs:
        positions = 0
        for k in range(1, abs(i - j + 1)):
            positions += k
        lineup += positions
    fuel.append(lineup)
print(min(fuel))
