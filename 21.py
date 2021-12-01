mylist = []
foodlist = []
alergenList = []
with open("21-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        i = i.strip()
        i = i.replace(')', '')
        i = i.split(' (contains ')
        i[0] = i[0].split(' ')
        i[1] = i[1].split(', ')
        mylist.append(i)
        foodlist.extend(i[0])
        alergenList.extend(i[1])
        print(i)

print('----')
allergenDict = {}
for food in mylist:
    for allergen in food[1]:
        if allergen not in allergenDict:
            allergenDict[allergen] = food[0].copy()
        else:
            allergenDict[allergen] = [ingred for ingred in allergenDict[allergen] if ingred in food[0]]

print(allergenDict)
print(foodlist)
allergenSet = []
for x in allergenDict.values():
    allergenSet.extend(x)
allergenSet = set(allergenSet)
print(allergenSet)

count = 0
for item in foodlist:
    if item not in allergenSet:
        count += 1

print(count)
