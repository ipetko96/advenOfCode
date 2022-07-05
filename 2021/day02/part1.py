import re

horizontal, depth = 0, 0
with open('2021\\day02\\input', 'r') as file:
    for line in file:
        match = re.match(r'(\w+)\s(\d)', line)
        if match.group(1) == 'forward':
            horizontal += int(match.group(2))
        elif match.group(1) == 'down':
            depth += int(match.group(2))
        elif match.group(1) == 'up':
            depth -= int(match.group(2))
    print(horizontal * depth)
