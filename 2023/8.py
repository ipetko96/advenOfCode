with open("input") as file:
    lines = file.read()

instructions, nodes = lines.split("\n\n")
instructions = list(instructions)
nodes = nodes.split("\n")
nodes_dict = {}
for i in nodes:
    key, value = i.split(" = ")
    value = value[1:-1].split(", ")
    nodes_dict[key] = value


def rotate():
    global instructions
    instructions = instructions[1:] + instructions[:1]


counter = 0
node = "AAA"
while True:
    if node == "ZZZ":
        break
    else:
        counter += 1
        if instructions[0] == "R":
            rotate()
            node = nodes_dict[node][1]
            continue
        elif instructions[0] == "L":
            rotate()
            node = nodes_dict[node][0]
            continue

print(counter)
