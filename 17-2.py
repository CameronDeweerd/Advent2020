import copy
mylist = []
with open("17-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        mylist.append(i.strip())
print(mylist)

# each cycle can add 2 more length+width (8+12)and 2 more height(1 + 12)
# we add another 2 to each side for a buffer to avoid dealing w/ index overflow
line = []
plane = []
cube = []
hyper = []
for _ in range(22):
    line.append('.')
for _ in range(22):
    plane.append(copy.copy(line))
for _ in range(15):
    cube.append(copy.deepcopy(plane))
for _ in range(15):
    hyper.append(copy.deepcopy(cube))

for rowNum, rowVal in enumerate(mylist):
    for columnNum, columnVal in enumerate(rowVal):
        hyper[7][7][7+rowNum][7+columnNum] = columnVal


def checkFlip(x, y, z, h, hyper):
    count = 0
    for xOffset in (-1,0,1):
        for yOffset in (-1,0,1):
            for zOffset in (-1,0,1):
                for hOffset in (-1, 0, 1):
                    if hyper[h+hOffset][z+zOffset][y+yOffset][x+xOffset] == '#':
                        count += 1
    if hyper[h][z][y][x] == '#':
        # count -= 1
        if count == 3 or count == 4:
            return False
        else:
            return True
    else:
        if count == 3:
            return True
        else:
            return False


for loop in range(6):
    flip = []
    for x in range(1,21):
        for y in range(1, 21):
            for z in range(1, 14):
                for h in range(1, 14):
                    if checkFlip(x, y, z, h, hyper):
                        flip.append((x,y,z,h))

    for x,y,z,h in flip:
        if hyper[h][z][y][x] == '#':
            hyper[h][z][y][x] = '.'
        else:
            hyper[h][z][y][x] = '#'

pass

total = 0
for x in range(1, 21):
    for y in range(1, 21):
        for z in range(1, 14):
            for h in range(1, 14):
                if hyper[h][z][y][x] == '#':
                    total += 1

print(total)
