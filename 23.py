myInput = [9, 7, 4, 6, 1, 8, 3, 5, 2]
testInput = [3, 8, 9, 1, 2, 5, 4, 6, 7]


class cup:
    def __init__(self, number, right, left):
        self.number = number
        self.right = right
        self.left = left


def swap(input):
    # Select target
    target = input[0]

    # pick up next 3 cups
    pickedUp = [input.pop(1), input.pop(1), input.pop(1)]

    # calculate destination cup
    destination = target - 1
    while True:
        if destination == 0:
            destination = len(input + 3)
        if destination in pickedUp:
            destination = destination - 1
        else:
            break

    # find destination cup
    destIndex = input.index(destination)

    # place picked up cups
    input.insert(destIndex + 1, pickedUp[2])
    input.insert(destIndex + 1, pickedUp[1])
    input.insert(destIndex + 1, pickedUp[0])

    # select next cup
    input.append(input.pop(0))
    return input


def looper(loopCount, input):
    for x in range(loopCount):
        input = swap(input)

    index = input.index(1)
    if len(input) < 100:
        before = input[0:index]
        after = input[index + 1:]
        print(after, before)
    else:
        print(input[index + 1:index + 3])


milMyInput = myInput[:]
milTestInput = testInput[:]
for x in range(10, 1000000):
    milMyInput.append(x)
    milTestInput.append(x)

looper(10, testInput)
looper(100, myInput)
looper(10, milTestInput)
looper(1000, milMyInput)
