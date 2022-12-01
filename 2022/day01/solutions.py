elf_callories = set()
callories_count = 0

with open("2022\\day01\\input", "r") as file:
    for line in file:
        if line.strip() != "":
            callories_count += int(line)
            continue
        elf_callories.add(callories_count)
        callories_count = 0

# part 1
print(max(elf_callories))

# part 2
sorted_elf_callories = sorted(elf_callories)
print(sum(sorted_elf_callories[-3:]))
