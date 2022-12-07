with open("2022\\day06\\input", "r") as file:
    stream = file.read()


def find_index(count: int) -> int:
    return [i + count for i in range(len(stream)) if len(set(stream[i:i + count])) == count][0]


# part 1
print(find_index(4))

# part 2
print(find_index(14))
