wires = {}
operators = {
    "text": ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"],
    "bitwise": ["&", "|", "<<", ">>", "(1<<numbits)-1-"],
}
numbits = 16


def parseInput(line: str) -> None:
    splitedLine = line.strip().split(" -> ")
    if splitedLine[0].isdigit():
        wires[splitedLine[1]] = {"signal": int(splitedLine[0]), "instructions": None}
    else:
        wires[splitedLine[1]] = {"signal": None, "instructions": splitedLine[0]}


def checkSignal(wire: str) -> bool:
    if getSignal(wire) is None:
        return False
    else:
        return True


def getSignal(wire: str) -> int:
    return wires[wire]["signal"]


def isLowercase(element: str) -> bool:
    return element.islower()


def getWires(wire: str) -> list:
    instructions = wires[wire]["instructions"].split()
    return list(filter(isLowercase, instructions))


def solveSignal(wire: str) -> None:
    if checkSignal(wire):
        return
    else:
        replaceWire(wire)
        replaceOperator(wire)
        wires[wire]["signal"] = int(eval(getInstructions(wire)))


def getInstructions(wire: str) -> str:
    return wires[wire]["instructions"]


def replaceOperator(wire: str) -> None:
    for i in range(len(operators["text"])):
        if operators["text"][i] in wires[wire]["instructions"]:
            wires[wire]["instructions"] = wires[wire]["instructions"].replace(
                operators["text"][i], operators["bitwise"][i]
            )
            return


def replaceWire(wire: str) -> None:
    for knownWire in getWires(wire):
        wires[wire]["instructions"] = wires[wire]["instructions"].replace(
            knownWire, str(wires[knownWire]["signal"])
        )


def findWireSignal(wire: str) -> str:
    if checkSignal(wire):
        return getSignal(wire)
    else:
        for unknownWire in getWires(wire):
            if checkSignal(unknownWire):
                continue
            else:
                findWireSignal(unknownWire)
        solveSignal(wire)


with open("2015/day07/input", "r") as file:
    for line in file:
        parseInput(line)
    print()

findWireSignal("a")
print(getSignal("a"))
