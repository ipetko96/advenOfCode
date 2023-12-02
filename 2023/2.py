import re

games = 0
with open("input") as file:
    lines = file.readlines()
for i in lines:
    line = i.split(":")
    game_id = int(line[0].split()[1])
    red = re.findall(r"\d+ red", i)
    green = re.findall(r"\d+ green", i)
    blue = re.findall(r"\d+ blue", i)
    red_num = re.findall(r"\d+", "".join(red))
    green_num = re.findall(r"\d+", "".join(green))
    blue_num = re.findall(r"\d+", "".join(blue))
    red_num_int = list(map(int, red_num))
    green_num_int = list(map(int, green_num))
    blue_num_int = list(map(int, blue_num))
    if max(red_num_int) <= 12 and max(green_num_int) <= 13 and max(blue_num_int) <= 14:
        games += game_id
print(games)

games = 0
with open("input") as file:
    lines = file.readlines()
for i in lines:
    line = i.split(":")
    game_id = int(line[0].split()[1])
    red = re.findall(r"\d+ red", i)
    green = re.findall(r"\d+ green", i)
    blue = re.findall(r"\d+ blue", i)
    red_num = re.findall(r"\d+", "".join(red))
    green_num = re.findall(r"\d+", "".join(green))
    blue_num = re.findall(r"\d+", "".join(blue))
    red_num_int = list(map(int, red_num))
    green_num_int = list(map(int, green_num))
    blue_num_int = list(map(int, blue_num))
    power = max(red_num_int) * max(green_num_int) * max(blue_num_int)
    games += power
print(games)
