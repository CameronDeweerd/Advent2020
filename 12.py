'''
--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
'''

mylist = []
with open("12-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        command = i.strip()
        mylist.append((command[0], int(command[1:])))
print(mylist)

# part 1 #

EW=0
NS=0
head=0

for command, distance in mylist:
    if command == 'N':
        NS += distance
    elif command == 'S':
        NS += -1*distance
    elif command == 'E':
        EW += distance
    elif command == 'W':
        EW += -1*distance
    elif command == 'L':
        head += distance
    elif command == 'R':
        head += -1*distance
    elif command == 'F':
        if head % 360 == 0:
            EW += distance
        elif head % 360 == 90:
            NS += distance
        elif head % 360 == 180:
            EW += -1*distance
        elif head % 360 == 270:
            NS += -1*distance
print(NS, EW)


# part 2 #

target = [1, 10]
current = [0, 0]

for command, distance in mylist:
    if command == 'N':
        target[0] += distance
    elif command == 'S':
        target[0] += -1*distance
    elif command == 'E':
        target[1] += distance
    elif command == 'W':
        target[1] += -1*distance
    elif command == 'R':
        for i in range(int(distance/90)):
            target.reverse()
            target[0] *= -1
    elif command == 'L':
        for i in range(int(distance/90)):
            target.reverse()
            target[1] *= -1
    elif command == 'F':
        current[0] += target[0] * distance
        current[1] += target[1] * distance
    print(command, distance, target, current)

print(current, abs(current[0]) + abs(current[1]))
