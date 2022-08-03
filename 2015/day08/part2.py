import json

lenWithQuotes, lenEncoded = 0, 0

with open("2015\\day08\\input", "r") as file:
    for line in file:
        lenWithQuotes += len(line[:-1])
        lenEncoded += len(json.dumps(line[:-1]))
    print(lenEncoded - lenWithQuotes)
