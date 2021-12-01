
mylist = []
with open("16-1-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        mylist.append(i.strip())
print(mylist)

details = []
with open("16-3-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        details.append(i.strip())
print(details)

legalRanges = []
for item in details:
    x = item.find(':')
    numString = item[x+2:].split(' or ')
    for i in numString:
        legalRanges.append(i.split('-'))
print(legalRanges)

legal = {}
for legalRange in legalRanges:
    for num in range(int(legalRange[0]), int(legalRange[1])+1):
        legal[num] = True
print(legal)

errorSum = 0
legalTickets = []
for ticketVals in mylist:
    islegal = True
    for ticketVal in ticketVals.split(','):
        try:
            x = legal[int(ticketVal)]
        except KeyError:
            errorSum += int(ticketVal)
            islegal = False
    if islegal:
        legalTickets.append(ticketVals)
print(errorSum)

splitLegal = []
for count, legalRange in enumerate(legalRanges):
    if count % 2 == 0:
        legal = {}
        for num in range(int(legalRange[0]), int(legalRange[1])+1):
            legal[num] = True
    else:
        for num in range(int(legalRange[0]), int(legalRange[1])+1):
            legal[num] = True
        splitLegal.append(legal)

possible = []
for ticketColumn in range(len(legalTickets[0].split(','))):
    possible.append([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    for ticket in legalTickets:
        val = ticket.split(',')[ticketColumn]
        for possibleColumn in reversed(possible[ticketColumn]):
            try:
                x = splitLegal[possibleColumn][int(val)]
            except KeyError:
                possible[ticketColumn].remove(possibleColumn)
final={}
while len(final) < 20:
    for count, column in enumerate(possible):
        if len(column) == 1:
            final[count] = column[0]
            for x in possible:
                try:
                    x.remove(final[count])
                except ValueError:
                    pass
print(final)
myticket = [53,101,83,151,127,131,103,61,73,71,97,89,113,67,149,163,139,59,79,137]
print(myticket[2] * myticket[16] * myticket[5] * myticket[1] * myticket[17] * myticket[13])
