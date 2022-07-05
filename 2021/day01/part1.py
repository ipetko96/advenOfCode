increased, previous = 0, 999
with open('2021\\day01\\input', 'r') as file:
    for line in file:
        line = int(line.rstrip())
        if line > previous:
            increased += 1
        previous = line
    print(increased)
