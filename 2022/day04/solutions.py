file_length = 0
contained = 0
non_overlap = 0
with open("2022\\day04\\input", "r") as file:
    for line in file:
        file_length += 1
        line = line.strip().replace(",", "-")
        a, b, c, d = line.split("-")
        if int(c) >= int(a) and int(d) <= int(b):
            contained += 1
        elif int(a) >= int(c) and int(b) <= int(d):
            contained += 1
        if int(b) < int(c):
            non_overlap += 1
        elif int(a) > int(d):
            non_overlap += 1

overlap = file_length - non_overlap

# part 1
print(contained)

# part 2
print(overlap)
