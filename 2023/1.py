import re

count = 0
with open("input") as file:
    lines = file.readlines()
for i in lines:
    numbers = re.findall(r"\d", i)
    create_number = f"{numbers[0]}{numbers[-1]}"
    count += int(create_number)

print(count)

count = 0
with open("input") as file:
    lines = file.readlines()
for i in lines:
    i = i.replace("one", "o1e")
    i = i.replace("two", "t2o")
    i = i.replace("three", "t3e")
    i = i.replace("four", "f4r")
    i = i.replace("five", "f5e")
    i = i.replace("six", "s6x")
    i = i.replace("seven", "s7n")
    i = i.replace("eight", "e8t")
    i = i.replace("nine", "n9e")
    numbers = re.findall(r"\d", i)
    numbers = [i for numbers in numbers for i in numbers]
    numbers = [x for x in numbers if x]
    create_number = f"{numbers[0]}{numbers[-1]}"
    count += int(create_number)

print(count)
