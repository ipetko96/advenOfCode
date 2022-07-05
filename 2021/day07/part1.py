with open('2021\\day07\\tinput', 'r') as file:
    crabs = [int(number) for number in file.readline().split(',')]

fuel = []
for j in range(len(crabs)):
    positions = 0
    for i in crabs:
        positions += abs(i - j)
    fuel.append(positions)
print(min(fuel))
