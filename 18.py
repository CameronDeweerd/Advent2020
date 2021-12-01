mylist = []
with open("18-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        i = i.strip()
        i = i.replace(' ', '')
        i = list(i)
        mylist.append(i)
print(mylist)


# part 1

def math(arguement):
    currentVal = arguement.pop(0)
    if currentVal == '(':
        close = findClose(arguement)
        currentVal = math(arguement[0:close])
        for x in range(close + 1):
            arguement.pop(0)
    operator = ''
    while arguement:
        if operator == '':
            operator = arguement.pop(0)
        # elif char == '(':
        #     close = findClose(arguement[index:])
        #     currentVal = math(arguement[1:close])
        else:
            nextNum = arguement.pop(0)
            if nextNum == '(':
                close = findClose(arguement)
                nextNum = math(arguement[0:close])
                for x in range(close + 1):
                    arguement.pop(0)
            if operator == '*':
                currentVal = str(int(currentVal) * int(nextNum))
            else:
                currentVal = str(int(currentVal) + int(nextNum))
            operator = ''
    return currentVal


def findClose(argument, openCount=1):
    for index, char in enumerate(argument):
        if char == '(':
            openCount += 1
        elif char == ')':
            openCount -= 1
            if openCount == 0:
                return index


x = math(list('5*9*(7*3*3+9*3+(8+6*4))'))
print(x)


# total = 0
# for equation in mylist:
#     x = int(math(equation))
#     print(x)
#     total += x
#
# print(total)


# part 2

def flipMath(argument):
    for index, char in enumerate(argument):
        if char == '(':
            close = findClose(argument[index:], 0)
            argument[index] = flipMath(argument[index + 1:index + close])
            for _ in range(close):
                argument.pop(index + 1)

    for index, char in reversed(list(enumerate(argument))):
        if char == '+':
            argument[index - 1] = str(int(argument[index - 1]) + int(argument[index + 1]))
            argument.pop(index)
            argument.pop(index)
    for index, char in reversed(list(enumerate(argument))):
        if char == '*':
            argument[index - 1] = str(int(argument[index - 1]) * int(argument[index + 1]))
            argument.pop(index)
            argument.pop(index)
    currentVal = argument[0]
    return currentVal


assert flipMath(list('2*3+(4*5)')) == '46', 'result should be 46'
assert flipMath(list('5*9*(7*3*3+9*3+(8+6*4))')) == '669060', 'result should be 669060'

total = 0
for equation in mylist:
    x = int(flipMath(equation))
    print(x)
    total += x

print(total)
