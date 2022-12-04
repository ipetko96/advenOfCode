from difflib import SequenceMatcher

# part 1
count = 0
with open("2022\\day03\\input", "r") as file:
    for line in file:
        line = line.strip()
        a, b = line[:len(line) // 2], line[len(line) // 2:]
        match = SequenceMatcher(None, a, b).find_longest_match()
        answer = a[match.a:match.a + match.size]
        if answer.isupper():
            count += ord(answer[0]) - 38
        else:
            count += ord(answer[0]) - 96

print(count)

# part 2
rucksacks = []
count = 0
with open("2022\\day03\\input", "r") as file:
    for line in file:
        rucksacks.append(line.strip())

for i in range(0, len(rucksacks), 3):
    sublist = []
    sublist.append(rucksacks[i])
    sublist.append(rucksacks[i + 1])
    sublist.append(rucksacks[i + 2])
    for j in min(sublist):
        if j in rucksacks[i] and j in rucksacks[i + 1] and j in rucksacks[i + 2]:
            if j.isupper():
                count += ord(j) - 38
                break
            else:
                count += ord(j) - 96
                break

print(count)
