with open('2021\\day03\\input', 'r') as file:
    numbers = file.read().splitlines()


def ruleBit(numbers, position, bit):
    zeroCount, oneCount = 0, 0
    for line in numbers:
        if line[position] == '0':
            zeroCount += 1
        elif line[position] == '1':
            oneCount += 1
    if bit == 0:
        if zeroCount < oneCount:
            return 0
        elif oneCount < zeroCount:
            return 1
        elif zeroCount == oneCount:
            return bit
    elif bit == 1:
        if zeroCount > oneCount:
            return 0
        elif oneCount > zeroCount:
            return 1
        elif zeroCount == oneCount:
            return bit


def shrinkNumbers(numbers, bit, position):
    rule = ruleBit(numbers, position, bit)
    for i in range(len(numbers) - 1, -1, -1):
        if int(numbers[i][position]) != rule:
            numbers.pop(i)
    if len(numbers) != 1:
        shrinkNumbers(numbers, bit, position + 1)
    else:
        return numbers[0]


print(int(shrinkNumbers(numbers, 1, 0), 2) * int(shrinkNumbers(numbers, 0, 0), 2))
