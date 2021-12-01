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
for _ in range(22):
    line.append('.')
for _ in range(22):
    plane.append(copy.copy(line))
for _ in range(15):
    cube.append(copy.deepcopy(plane))

for rowNum, rowVal in enumerate(mylist):
    for columnNum, columnVal in enumerate(rowVal):
        cube[7][7+rowNum][7+columnNum] = columnVal


def checkFlip(x, y, z, cube):
    count = 0
    for xOffset in (-1,0,1):
        for yOffset in (-1,0,1):
            for zOffset in (-1,0,1):
                if cube[z+zOffset][y+yOffset][x+xOffset] == '#':
                    count += 1
    if cube[z][y][x] == '#':
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
                if checkFlip(x, y, z, cube):
                    flip.append((x,y,z))

    for x,y,z in flip:
        if cube[z][y][x] == '#':
            cube[z][y][x] = '.'
        else:
            cube[z][y][x] = '#'

pass

total = 0
for x in range(1, 21):
    for y in range(1, 21):
        for z in range(1, 14):
            if cube[z][y][x] == '#':
                total += 1

print(total)
