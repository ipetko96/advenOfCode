areaSum = 0
areas = []

with open("2015\day02\input", "r") as file:
    for line in file:
        data = line.strip().split("x")
        data = list(map(int, data))
        areas.append(data[0] * data[1])
        areas.append(data[1] * data[2])
        areas.append(data[2] * data[0])
        smallestArea = min(areas)
        areaSum += (2 * data[0] * data[1]) + (2 * data[1] * data[2]) + (2 * data[2] * data[0]) + min(areas)
        areas.clear()
print(areaSum)
