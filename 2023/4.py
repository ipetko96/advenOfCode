lines = []
cards_sum = []
with open("input") as file:
    for line in file:
        line = line.strip().split(":")
        line = "".join(line[1])
        line = line.strip().split("|")
        lines.append(line)
        cards_sum.append(1)

points = 0
counter = 0
counter2 = 0
for i, line in enumerate(lines):
    winning = line[0].strip().split()
    picked = line[1].strip().split()
    for j in picked:
        if j in winning:
            counter2 += 1
            if counter == 0:
                counter += 1
            else:
                counter *= 2
    points += counter
    counter = 0
    if counter2 == 0:
        continue
    count = cards_sum[i]
    for k in range(i + 1, i + counter2 + 1):
        cards_sum[k] += count
    counter2 = 0
print(points)
print(sum(cards_sum))
