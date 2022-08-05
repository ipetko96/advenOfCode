bags = {}
canContain = set()

with open("2020\\day07\\input", "r") as file:
    for line in file:
        line = line.strip().replace(" bags", "").split(" contain ")
        bags[line[0]] = line[1]


def searchBag(bag: str) -> None:
    for newBag in bags:
        if bag in bags[newBag]:
            searchBag(newBag)
            canContain.add(newBag)
    return


searchBag("shiny gold")
print(len(canContain))
