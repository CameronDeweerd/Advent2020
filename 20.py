class Tile:
    def __init__(self, ID, up, right, down, left, internal):
        self.ID = int(ID[-5:-1])
        self.up = up
        self.right = right
        self.down = down
        self.left = left
        self.side = 1
        self.grid = None
        self.rotation = 0
        self.internal = internal

    def rotate(self):
        x = self.up[::-1]
        self.up = self.right
        self.right = self.down[::-1]
        self.down = self.left
        self.left = x
        self.internal = list(zip(*self.internal))[::-1]

    def flip(self):
        x = self.up
        self.right = self.right[::-1]
        self.up = self.down
        self.left = self.left[::-1]
        self.down = x
        self.side = self.side * -1
        self.internal = self.internal[::-1]

    def getSides(self):
        return self.up, self.right, self.down, self.left


mylist = []
with open("20-input.txt", "r") as f:  # log.txt file has line separated values,
    tiles = f.read().split('\n\n')
    for tile in tiles:
        lines = tile.split('\n')
        ID = lines[0]
        top = lines[1]
        bottom = lines[10]
        left = ""
        right = ""
        internal = []
        for x in range(1, 11):
            left = left + lines[x][0]
            if 1 < x < 10:
                internal.append(list(lines[x][1:9]))
            right = right + lines[x][9]
        mylist.append(Tile(ID, top, right, bottom, left, internal))

print(mylist)
grid = {}
grid[(0, 0)] = mylist[0]
mylist[0].grid = (0, 0)
mylist.pop(0)


# for tile in mylist.keys():
#     for side in mylist[tile]:
#         matches[side] += 1
#
# print(matches)

def checkMatchNorth(target, tile):
    for flip in range(2):
        for rotate in range(4):
            if tile.down == target:
                return True
            tile.rotate()
        tile.flip()
    return False


def checkMatchSouth(target, tile):
    for flip in range(2):
        for rotate in range(4):
            if tile.up == target:
                return True
            tile.rotate()
        tile.flip()
    return False


def checkMatchEast(target, tile):
    for flip in range(2):
        for rotate in range(4):
            if tile.left == target:
                return True
            tile.rotate()
        tile.flip()
    return False


def checkMatchWest(target, tile):
    for flip in range(2):
        for rotate in range(4):
            if tile.right == target:
                return True
            tile.rotate()
        tile.flip()
    return False


gridList = [(0, 0)]
for x, y in gridList:
    if (x, y - 1) not in grid:
        target = grid[(x, y)].up
        for index, tile in enumerate(mylist):
            if checkMatchNorth(target, tile):
                grid[(x, y - 1)] = tile
                tile.grid = (x, y - 1)
                mylist.pop(index)
                gridList.append((x, y - 1))
                break
    if (x, y + 1) not in grid:
        target = grid[(x, y)].down
        for index, tile in enumerate(mylist):
            if checkMatchSouth(target, tile):
                grid[(x, y + 1)] = tile
                tile.grid = (x, y + 1)
                mylist.pop(index)
                gridList.append((x, y + 1))
                break
    if (x - 1, y) not in grid:
        target = grid[(x, y)].left
        for index, tile in enumerate(mylist):
            if checkMatchWest(target, tile):
                grid[(x - 1, y)] = tile
                tile.grid = (x - 1, y)
                mylist.pop(index)
                gridList.append((x - 1, y))
                break
    if (x + 1, y) not in grid:
        target = grid[(x, y)].right
        for index, tile in enumerate(mylist):
            if checkMatchEast(target, tile):
                grid[(x + 1, y)] = tile
                tile.grid = (x + 1, y)
                mylist.pop(index)
                gridList.append((x + 1, y))
                break
print(grid)
coordinates = list(grid.keys())
x0 = 0
x1 = 0
y0 = 0
y1 = 0

for x, y in coordinates:
    x0 = x if x < x0 else x0
    x1 = x if x > x1 else x1
    y0 = y if y < y0 else y0
    y1 = y if y > y1 else y1

print(grid[(x0, y0)].ID, grid[(x1, y0)].ID, grid[(x0, y1)].ID, grid[(x1, y1)].ID)
print(grid[(x0, y0)].ID * grid[(x1, y0)].ID * grid[(x0, y1)].ID * grid[(x1, y1)].ID)

count = 0
photo = []
for y in range(y0, y1 + 1):
    for row in range(8):
        line = []
        for x in range(x0, x1 + 1):
            line.extend(grid[(x, y)].internal[row])
        count += line.count('#')
        photo.append(line)
print(photo)
print(count)

monster = 0
for x in range(77):
    for y in range(94):
        for monsterx, monstery in (
        (0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 1),
        (18, 0), (19, 1)):
            if photo[x + monsterx][y + monstery] == '.':
                break
        else:
            monster += 1

print(monster)
