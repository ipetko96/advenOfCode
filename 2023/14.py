import re

pole = []
with open("input") as file:
    for line in file.readlines():
        pole.append(list(line.strip()))
rotated = list(zip(*pole[::-1]))

for index, line in enumerate(rotated):
    line1 = "".join(line)
    line2 = re.split(r"(#)", line1)
    for i, v in enumerate(line2):
        line2[i] = "".join(sorted(v))
    line3 = ""
    for i in line2:
        if i == "":
            continue
        else:
            line3 += "".join(i)
    rotated[index] = list(line3)
unrotate = list(zip(*rotated[::-1]))
count = 0
for i, v in enumerate(unrotate):
    count += "".join(v).count("O") * (i + 1)
print(count)
