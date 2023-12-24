pole=[]
with open('input') as file:
    for line in file.readlines():
        pole.append(list(line.strip()))
rotated = list(zip(*pole[::-1]))

for index,line in enumerate(rotated):
    line1= ''.join(line)
    line2=line1.split('#')
    for i,v in enumerate(line2):
        line2[i]=''.join(sorted(v))
    line3=''
    for i in line2:
        if i == '':
            line3 += '#'
        else:
            line3+= ''.join(i)
    rotated[index]= line3
...