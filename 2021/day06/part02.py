import time
start_time = time.time()

zadanie = []

with open('2021\\day06\\input', 'r') as file:
    zadanie = [int(number) for number in file.readline().split(',')]

ryby = [0] * 9
for ryba in zadanie:
    ryby[ryba] += 1

for day in range(750000):
    ryby.append(ryby.pop(0))
    ryby[6] += ryby[8]

print(sum(ryby))
print("--- %s seconds ---" % (time.time() - start_time))
