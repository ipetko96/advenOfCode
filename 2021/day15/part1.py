board = []
rules = []
unvisited = []
bigNumber = 999

with open('2021\\day15\\tinput', 'r') as file:
    for line in file:
        board.append(list(line.strip()))

for i in range(len(board)):
    for j, value in enumerate(board[i]):
        if i == 0 and j == 0:
            rules.append({"vertex": [i, j], "shortest": 0, "previous": ""})
        else:
            rules.append(
                {"vertex": [i, j],"value": board[i][j], "shortest": bigNumber, "previous": []})
        unvisited.append([i, j])
print()


def get_horizontal_and_vertical_neighbours(arr, x, y):
    """
    This method takes 2d array and return list of all elements
    with all horizontal and vertical neighbours
    :param arr: 2d array
    :return: list of array elements with neighbours
    """
    neighbors = []

    if x == 0 or x == len(arr) - 1 or y == 0 or y == len(arr[x]) - 1:
        # corners
        new_neighbors = []
        if x != 0:
            new_neighbors.append({"vertex": [x - 1][y], "value": arr[x - 1][y]})  # top neighbor
        if y != len(arr[x]) - 1:
            new_neighbors.append({"vertex": [x][y + 1], "value": arr[x][y + 1]})  # right neighbor
        if x != len(arr) - 1:
            new_neighbors.append({"vertex": [x + 1][y], "value": arr[x + 1][y]})  # bottom neighbor
        if y != 0:
            new_neighbors.append({"vertex": [x][y - 1], "value": arr[x][y - 1]})  # left neighbor

    else:
        # add neighbors
        new_neighbors = [{
            arr[x - 1][y],  # top neighbor
            arr[x][y + 1],  # right neighbor
            arr[x + 1][y],  # bottom neighbor
            arr[x][y - 1]   # left neighbor
        }]

        new_neighbors.append({
            "index": x * len(arr[x]) + j,
            "value": value,
            "neighbors": new_neighbors,
            "shortestPath": 999})

    return neighbors


while len(unvisited) != 0:
    currenVertex = unvisited[0]
    for neighbor in get_horizontal_and_vertical_neighbours(board, currenVertex[0], currenVertex[1]):
        print(neighbor)

    # for i in range(len(board)):
    #     for j, value in enumerate(board[i]):
    #         for neighbor in get_horizontal_and_vertical_neighbours(board, i, j):
    #             if neighbor <= bigNumber:
    #                 rules.append({"asd": 123})
