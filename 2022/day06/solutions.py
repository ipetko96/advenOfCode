with open("2022\\day06\\input", "r") as file:
    stream = file.read()


def find_index(count: int) -> int:
    index = 0
    while len(set(stream[index:index + count])) != count:
        index += 1
    return index + count


# part 1
print(find_index(4))

# part 2
print(find_index(14))
