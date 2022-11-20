cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
base = 1
cups_without_pick_up = cups[base:] + cups[:base]
pick_up = cups_without_pick_up[:3]
del cups_without_pick_up[:3]
destination_cup = cups[0] - 1
while destination_cup in pick_up:
    destination_cup -= 1
    if destination_cup < min(cups_without_pick_up):
        destination_cup = max(cups_without_pick_up)
print(cups)
print(pick_up)
print(destination_cup)
print(cups_without_pick_up)
# cups = cups_without_pick_up[5:] + cups_without_pick_up[:5]
cups_without_pick_up[destination_cup-1:destination_cup-1] = pick_up
# print(cups)
print(cups_without_pick_up)
