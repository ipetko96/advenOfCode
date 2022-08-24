import itertools


airports = set()
distances = {}
routeLengths = []

with open("2015\\day09\\input", "r") as file:
    for line in file:
        splitted = line.strip().split("=")
        onlyAirports = splitted[0].strip().split(" to ")
        for i in splitted[0].split("to"):
            airports.add(i.strip())
        distances[(onlyAirports[0], onlyAirports[1])] = int(splitted[1])
        distances[(onlyAirports[1], onlyAirports[0])] = int(splitted[1])

allPossiblePaths = list(itertools.permutations(airports))

for path in allPossiblePaths:
    routeLength = 0
    for i in range(len(path) - 1):
        routeLength += distances[(path[i], path[i + 1])]
    routeLengths.append(routeLength)

print(max(routeLengths))
