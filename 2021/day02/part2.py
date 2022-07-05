import re

horizontal, depth, aim = 0, 0, 0
with open('2021\\day02\\input', 'r') as file:
    for line in file:
        match = re.match(r'(\w+)\s(\d)', line)
        if match.group(1) == 'down':
            aim += int(match.group(2))
        elif match.group(1) == 'up':
            aim -= int(match.group(2))
        elif match.group(1) == 'forward':
            horizontal += int(match.group(2))
            depth += aim * int(match.group(2))
    print(horizontal * depth)
