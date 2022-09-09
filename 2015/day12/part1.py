import re

with open("2015\\day12\\tinput") as file:
    data = re.findall(r"-?\d+", file.read())
    print(sum(list(map(int, data))))
