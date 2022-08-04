import re

shinyGoldBags = 0
bags = {}

with open("2020\\day01\\input", "r") as file:
    for line in file:
        splitted = (
            line.strip()
            .replace("contain", "")
            .replace(",", "")
            .split(
                "bag",
            )
        )
        if "no other" in line:
            bags[splitted[0].strip()] = {"contain": None}
        else:
            bags[splitted[0].strip()] = {"contain": {"name": [], "count": []}}
            for element in splitted[1:-1]:
                match = re.match(r".*(\d+)\s([\w\s]+)", element.strip())
                bags[splitted[0].strip()]["contain"]["name"].append(match.group(2))
                bags[splitted[0].strip()]["contain"]["count"].append(match.group(1))
