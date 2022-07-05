from itertools import count
import hashlib

with open("2015\day04\input", "r") as file:
    PUZZLE_INPUT = file.readline()


def findHash(input: str, match: str):
    for i in count(1):
        guessedHash = hashlib.md5((input + str(i)).encode("utf-8")).hexdigest()
        if guessedHash[: len(match)] == match:
            return i


print(findHash(PUZZLE_INPUT, "00000"))
