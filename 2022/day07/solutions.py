filesystem = {}

with open("2022\\day07\\tinput", "r") as file:
    for line in file:
        if "$" in line:
            if "cd" in line:
                _, _, pwd = line.strip().split()

            print(line.strip())
