import json

with open("2015\\day12\\input") as file:
    data = json.loads(file.read())

sum = 0


def dive(obj) -> None:
    global sum
    subSum = 0
    if isinstance(obj, dict) and "red" in obj.values():
        return
    else:
        if isinstance(obj, dict):
            for key in obj:
                if isinstance(obj[key], dict):
                    dive(obj[key])
                elif isinstance(obj[key], list):
                    dive(obj[key])
                elif isinstance(obj[key], int):
                    subSum += obj[key]
                else:
                    continue
        else:
            for i in range(len(obj)):
                if isinstance(obj[i], dict):
                    dive(obj[i])
                elif isinstance(obj[i], list):
                    dive(obj[i])
                elif isinstance(obj[i], int):
                    subSum += obj[i]
                else:
                    continue
        sum += subSum


dive(data)
print(sum)
