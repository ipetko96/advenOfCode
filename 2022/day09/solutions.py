head_pos = [0, 0]
tail_pos = [0, 0]
tail_visited = set()

# part 1
with open("2022\\day09\\input") as file:
    for line in file:
        ins, val = line.strip().split()
        if ins in "RL":
            for _ in range(int(val)):
                if ins == "R":
                    head_pos[0] += 1
                    if abs(head_pos[0] - tail_pos[0]) > 1:
                        tail_pos[0] += 1
                        if head_pos[1] - tail_pos[1] == 1:
                            tail_pos[1] += 1
                        if head_pos[1] - tail_pos[1] == -1:
                            tail_pos[1] -= 1
                else:
                    head_pos[0] -= 1
                    if abs(head_pos[0] - tail_pos[0]) > 1:
                        tail_pos[0] -= 1
                        if head_pos[1] - tail_pos[1] == 1:
                            tail_pos[1] += 1
                        if head_pos[1] - tail_pos[1] == -1:
                            tail_pos[1] -= 1
                tail_visited.add(tuple(tail_pos))
        else:
            for _ in range(int(val)):
                if ins == "U":
                    head_pos[1] += 1
                    if abs(head_pos[1] - tail_pos[1]) > 1:
                        tail_pos[1] += 1
                        if head_pos[0] - tail_pos[0] == 1:
                            tail_pos[0] += 1
                        if head_pos[0] - tail_pos[0] == -1:
                            tail_pos[0] -= 1
                else:
                    head_pos[1] -= 1
                    if abs(head_pos[1] - tail_pos[1]) > 1:
                        tail_pos[1] -= 1
                        if head_pos[0] - tail_pos[0] == 1:
                            tail_pos[0] += 1
                        if head_pos[0] - tail_pos[0] == -1:
                            tail_pos[0] -= 1
                tail_visited.add(tuple(tail_pos))
print(len(tail_visited))
