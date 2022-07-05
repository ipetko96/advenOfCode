increased, previous = 0, 0
with open('2021\\day01\\input', 'r') as file:
    numbers = file.read().splitlines()
    for i in range(len(numbers) - 2):
        sucet = int(numbers[i]) + int(numbers[i + 1]) + int(numbers[i + 2])
        if i == 0:
            previous = sucet
            continue
        if sucet > previous:
            increased += 1
        previous = sucet
    print(increased)
