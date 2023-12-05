with open("input") as file:
    lines = file.read()


parts = lines.split("\n\n")
seed, *maps = parts
seed = list(map(int, seed.split()[1:]))
loc = seed[:]

for i in maps:
    i = i.split("\n")[1:]
    for index, k in enumerate(seed):
        for j in i:
            dst, src, size = j.split()
            if int(src) <= k < (int(src) + int(size)):
                loc[index] = k - int(src) + int(dst)
                break
            else:
                loc[index] = k
    seed = loc[:]
print(min(loc))
