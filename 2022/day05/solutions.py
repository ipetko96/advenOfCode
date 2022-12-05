# part 1
crates = [
    ["s", "l", "w"],
    ["j", "t", "n", "q"],
    ["s", "c", "h", "f", "j"],
    ["t", "r", "m", "w", "n", "g", "b"],
    ["t", "r", "l", "s", "d", "h", "q", "b"],
    ["m", "j", "b", "v", "f", "h", "r", "l"],
    ["d", "w", "r", "n", "j", "m"],
    ["b", "z", "t", "f", "h", "n", "d", "j"],
    ["h", "l", "q", "n", "b", "f", "t"],
]

with open("2022\\day05\\input", "r") as file:
    for line in file:
        _, move, _, fro, _, to = line.strip().split()
        for _ in range(int(move)):
            crates[int(to) - 1].append("".join(crates[int(fro) - 1][-1:]))
            del crates[int(fro) - 1][-1:]

top_crates = ["".join(i[-1:]) for i in crates]
print("".join(top_crates))

# part 2
crates = [
    ["s", "l", "w"],
    ["j", "t", "n", "q"],
    ["s", "c", "h", "f", "j"],
    ["t", "r", "m", "w", "n", "g", "b"],
    ["t", "r", "l", "s", "d", "h", "q", "b"],
    ["m", "j", "b", "v", "f", "h", "r", "l"],
    ["d", "w", "r", "n", "j", "m"],
    ["b", "z", "t", "f", "h", "n", "d", "j"],
    ["h", "l", "q", "n", "b", "f", "t"],
]

with open("2022\\day05\\input", "r") as file:
    for line in file:
        _, move, _, fro, _, to = line.strip().split()
        crates[int(to) - 1].extend(crates[int(fro) - 1][-int(move):])
        crates[int(fro) - 1][-int(move):] = []

top_crates = ["".join(i[-1:]) for i in crates]
print("".join(top_crates))
