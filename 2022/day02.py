score_map = {"X": 1, "Y": 2, "Z": 3}

# part 1
win_score = 0

with open("2022/input", "r") as file:
    for line in file:
        elf, me = line.strip().split()
        if (
            elf == "A"
            and me == "Y"
            or elf == "B"
            and me == "Z"
            or elf == "C"
            and me == "X"
        ):
            win_score += 6
            win_score += score_map[me]
        if (
            elf == "A"
            and me == "X"
            or elf == "B"
            and me == "Y"
            or elf == "C"
            and me == "Z"
        ):
            win_score += 3
            win_score += score_map[me]
        if (
            elf == "A"
            and me == "Z"
            or elf == "B"
            and me == "X"
            or elf == "C"
            and me == "Y"
        ):
            win_score += score_map[me]

print(win_score)

# part 2
win_score = 0

with open("2022/input", "r") as file:
    for line in file:
        elf, me = line.strip().split()
        if elf == "A" and me == "Z":
            win_score += score_map["Y"]
            win_score += 6
        elif elf == "B" and me == "Z":
            win_score += score_map["Z"]
            win_score += 6
        elif elf == "C" and me == "Z":
            win_score += score_map["X"]
            win_score += 6
        elif elf == "A" and me == "Y":
            win_score += score_map["X"]
            win_score += 3
        elif elf == "B" and me == "Y":
            win_score += score_map["Y"]
            win_score += 3
        elif elf == "C" and me == "Y":
            win_score += score_map["Z"]
            win_score += 3
        elif elf == "A" and me == "X":
            win_score += score_map["Z"]
        elif elf == "B" and me == "X":
            win_score += score_map["X"]
        elif elf == "C" and me == "X":
            win_score += score_map["Y"]

print(win_score)
