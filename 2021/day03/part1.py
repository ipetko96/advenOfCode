gama, epsilon = '', ''

with open('2021\\day03\\input', 'r') as file:
    numbers = file.read().splitlines()
    for i in range(len(numbers[0])):
        zeroCount, oneCount = 0, 0
        for line in numbers:
            if line[i] == '0':
                zeroCount += 1
            elif line[i] == '1':
                oneCount += 1
        if zeroCount > oneCount:
            gama += '1'
            epsilon += '0'
        elif oneCount > zeroCount:
            gama += '0'
            epsilon += '1'
    print(int(gama, 2) * int(epsilon, 2))
