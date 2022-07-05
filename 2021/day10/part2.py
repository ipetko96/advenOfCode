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
                invertedChunk
                return invertedChunk

        else:
            if line[i] == invertedChunk[0]:
                invertedChunk = invertedChunk[1:]
                if i == len(line) - 1:
                    return invertedChunk
                else:
                    continue
            else:
                return 'c' + line[i]


scores = []
with open('2021\\day10\\input', 'r') as file:
    for line in file:
        score = 0
        lineState = checkLine(line.strip())
        if lineState[0] != 'c':
            for bracket in lineState:
                if bracket == ')':
                    score *= 5
                    score += 1
                    lineState = lineState[1:]
                elif bracket == ']':
                    score *= 5
                    score += 2
                    lineState = lineState[1:]
                elif bracket == '}':
                    score *= 5
                    score += 3
                    lineState = lineState[1:]
                elif bracket == '>':
                    score *= 5
                    score += 4
                    lineState = lineState[1:]
            scores.append(score)
    scores.sort()
    print(scores[len(scores) // 2:(len(scores) // 2) + 1])
