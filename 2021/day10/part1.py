def checkLine(line):
    openChunk = '([{<'
    invertedChunk = ''
    for i in range(len(line)):
        if line[i] in openChunk:
            if line[i] == '(':
                invertedChunk = ')' + invertedChunk
            elif line[i] == '[':
                invertedChunk = ']' + invertedChunk
            elif line[i] == '{':
                invertedChunk = '}' + invertedChunk
            elif line[i] == '<':
                invertedChunk = '>' + invertedChunk
            if i == len(line) - 1:
                return True

        else:
            if i != len(line) - 1:
                if line[i] == invertedChunk[0]:
                    invertedChunk = invertedChunk[1:]
                    continue
                elif line[i] != invertedChunk[0]:
                    return line[i]
            else:
                return True


counter = 0
with open('2021\\day10\\input', 'r') as file:
    for line in file:
        lineState = checkLine(line.strip())
        if lineState:
            continue
        else:
            if lineState == ')':
                counter += 3
            elif lineState == ']':
                counter += 57
            elif lineState == '}':
                counter += 1197
            elif lineState == '>':
                counter += 25137
    print(counter)
