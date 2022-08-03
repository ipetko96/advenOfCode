lenWithQuotes, lenWithoutQuotes = 0, 0

with open("2015\\day08\\input", "r") as file:
    for line in file:
        lenWithQuotes += len(line[:-1])
        lenWithoutQuotes += len(eval(line))
    print(lenWithQuotes - lenWithoutQuotes)
