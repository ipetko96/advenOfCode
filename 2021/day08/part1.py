import re

digits = 0

with open('2021\\day08\\input', 'r') as file:
    for line in file:
        match = re.match(r'.+\|\s(\w+)\s(\w+)\s(\w+)\s(\w+)', line)
        for i in range(1, 5):
            compare = match.group(i)
            if len(compare) == 2:
                digits += 1
            elif len(compare) == 4:
                digits += 1
            elif len(compare) == 3:
                digits += 1
            elif len(compare) == 7:
                digits += 1
            else:
                continue
    print(digits)
