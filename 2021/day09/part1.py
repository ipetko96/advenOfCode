heightmap = []

with open('2021\\day09\\input', 'r') as file:
    for line in file:
        heightmap.append(list(map(int, line.strip())))

counter = 0

for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        if i == 0 and j == 0:
            if heightmap[i][j] < heightmap[i][j + 1] and heightmap[i][j] < heightmap[i + 1][j]:
                counter += heightmap[i][j] + 1
                continue
        elif i == 0 and j == len(heightmap[i]) - 1:
            if heightmap[i][j] < heightmap[i + 1][j] and heightmap[i][j] < heightmap[i][j - 1]:
                counter += heightmap[i][j] + 1
                continue
        elif i == 0:
            if heightmap[i][j] < heightmap[i][j + 1] and heightmap[i][j] < heightmap[i + 1][j] and heightmap[i][j] < heightmap[i][j - 1]:
                counter += heightmap[i][j] + 1
                continue
        elif j == 0:
            if heightmap[i][j] < heightmap[i][j + 1] and heightmap[i][j] < heightmap[i + 1][j] and heightmap[i][j] < heightmap[i - 1][j]:
                counter += heightmap[i][j] + 1
                continue
        elif j == len(heightmap[i]) - 1 and i != len(heightmap) - 1:
            if heightmap[i][j] < heightmap[i + 1][j] and heightmap[i][j] < heightmap[i][j - 1] and heightmap[i][j] < heightmap[i - 1][j]:
                counter += heightmap[i][j] + 1
                continue
        elif i == len(heightmap) - 1 and j == 0:
            if heightmap[i][j] < heightmap[i][j + 1] and heightmap[i][j] < heightmap[i - 1][j]:
                counter += heightmap[i][j] + 1
                continue
        elif i == len(heightmap) - 1 and j == len(heightmap[i]) - 1:
            if heightmap[i][j] < heightmap[i][j - 1] and heightmap[i][j] < heightmap[i - 1][j]:
                counter += heightmap[i][j] + 1
                continue
        elif i == len(heightmap) - 1:
            if heightmap[i][j] < heightmap[i][j + 1] and heightmap[i][j] < heightmap[i][j - 1] and heightmap[i][j] < heightmap[i - 1][j]:
                counter += heightmap[i][j] + 1
                continue
        else:
            if heightmap[i][j] < heightmap[i][j + 1] and heightmap[i][j] < heightmap[i + 1][j] and heightmap[i][j] < heightmap[i][j - 1] and heightmap[i][j] < heightmap[i - 1][j]:
                counter += heightmap[i][j] + 1
                continue
            else:
                continue
print(counter)
