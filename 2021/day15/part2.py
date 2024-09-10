def get_neighbors(arr, x, y):
    neighbors = []

    if y == 0 or y == len(arr) - 1 or x == 0 or x == len(arr[y]) - 1:
        # corners
        # fmt: off
        if y != 0:
            neighbors.append((y - 1, x))  # top neighbor
        if x != len(arr[y]) - 1:
            neighbors.append((y, x + 1))  # right neighbor
        if y != len(arr) - 1:
            neighbors.append((y + 1, x))  # bottom neighbor
        if x != 0:
            neighbors.append((y, x - 1))  # left neighbor
        # fmt: on

    else:
        # all four neighbors
        neighbors.extend(
            [
                (y - 1, x),  # top neighbor
                (y, x + 1),  # right neighbor
                (y + 1, x),  # bottom neighbor
                (y, x - 1),  # left neighbor
            ]
        )

    return neighbors


board = []
table = {}
unvisited = []
bigNumber = 9999

with open("2021/day15/tinput", "r") as file:
    for line in file:
        board.append(list(map(int, line.strip())))

# tile board horizontaly
for i in range(len(board)):
    size = len(board[i])
    for k in range(4):
        for j in range(size):
            board[i].append(board[i][j + k * len(board)] % 9 + 1)

# tile board verticaly
for i in range(len(board) * 4):
    board.append([k % 9 + 1 for k in board[i]])

# generate table and unvisited
for i in range(len(board)):
    for j, value in enumerate(board[i]):
        if i == 0 and j == 0:
            table.update({(i, j): [board[i][j], 0, None]})
        else:
            table.update({(i, j): [board[i][j], bigNumber, None]})
        unvisited.append((i, j))

# fmt: off
while len(unvisited) != 0:  # repeat until unvisited is empty
    current_node = unvisited[0]  # set first node as current
    neighbors = get_neighbors(board, current_node[1], current_node[0])  # get surounding neighbors for current node

    for neighbor in neighbors:  # iterate through neighbors
        if neighbor not in unvisited:  # check if node was already visited
            continue
        new_distance = table[current_node][1] + table[neighbor][0]  # calculate new_distance for the neighbor
        if new_distance < table[neighbor][1]:  # check if the new_distance is shorter then currently known distance in neighbor
            table[neighbor][1] = new_distance  # replace current distance for neighbor with new_distance
            table[neighbor][2] = current_node  # replace previous closest node for neighbr with current node
    unvisited.remove(current_node)  # remove current node from unvisited
print(list(table.values())[-1][1])  # print shortest path length from top-left to bottom-right
# fmt: on
