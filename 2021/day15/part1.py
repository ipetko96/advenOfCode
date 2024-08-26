board = []
table = []
unvisited = []
bigNumber = 999

with open("2021\\day15\\tinput", "r") as file:
    for line in file:
        board.append(list(line.strip()))

for i in range(len(board)):
    for j, value in enumerate(board[i]):
        if i == 0 and j == 0:
            table.append({"vertex": [i, j], "shortest": 0, "previous": ""})
        else:
            table.append(
                {
                    "vertex": [i, j],
                    "value": board[i][j],
                    "shortest": bigNumber,
                    "previous": [],
                }
            )
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

    if y == 0 or y == len(arr) - 1 or x == 0 or x == len(arr[y]) - 1:
        # corners
        if y != 0:
            neighbors.append(
                {"vertex": [y - 1, x], "value": arr[y - 1][x]}
            )  # top neighbor
        if x != len(arr[y]) - 1:
            neighbors.append(
                {"vertex": [y, x + 1], "value": arr[y][x + 1]}
            )  # right neighbor
        if y != len(arr) - 1:
            neighbors.append(
                {"vertex": [y + 1, x], "value": arr[y + 1][x]}
            )  # bottom neighbor
        if x != 0:
            neighbors.append(
                {"vertex": [y, x - 1], "value": arr[y][x - 1]}
            )  # left neighbor

    else:
        # add neighbors
        neighbors = [
            {
                arr[y - 1][x],  # top neighbor
                arr[y][x + 1],  # right neighbor
                arr[y + 1][x],  # bottom neighbor
                arr[y][x - 1],  # left neighbor
            }
        ]

    neighbors.append(
        {
            "index": x * len(arr[x]) + j,
            "value": value,
            "neighbors": neighbors,
            "shortestPath": 999,
        }
    )

    return neighbors


while len(unvisited) != 0:
    currenVertex = unvisited[0]
    for neighbor in get_horizontal_and_vertical_neighbours(
        board, currenVertex[1], currenVertex[0]
    ):
        print(neighbor)
    unvisited.remove(currenVertex)

    # for i in range(len(board)):
    #     for j, value in enumerate(board[i]):
    #         for neighbor in get_horizontal_and_vertical_neighbours(board, i, j):
    #             if neighbor <= bigNumber:
    #                 rules.append({"asd": 123})
