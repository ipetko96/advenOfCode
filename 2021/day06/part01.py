ryby = []

with open('2021\\day06\\input', 'r') as file:
    ryby = [int(number) for number in file.readline().split(',')]


def dayCycle(ryby):
    for i in range(len(ryby)):
        if ryby[i] == 0:
            ryby[i] = 6
            ryby.append(8)
        else:
            ryby[i] -= 1
    return ryby


for i in range(1, 256):
    dayCycle(ryby)
print(len(ryby))
