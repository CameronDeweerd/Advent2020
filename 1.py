'''
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
'''


list = []
with open("1-1-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        list.append(int(i.strip()))
print(list)

### part 1 ###

for i in range(len(list)):
    for j in range(i, len(list)):
        if list[i]+list[j] == 2020:
            print(list[i], list[j], list[i]*list[j])

### part 2 ###

for i in range(len(list)):
    for j in range(i, len(list)):
        for k in range(j, len(list)):
            if list[i]+list[j]+list[k] == 2020:
                print(list[i], list[j], list[k], list[i]*list[j]*list[k])
