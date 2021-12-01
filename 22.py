mylist = [[], []]
with open("22-input.txt", "r") as f:  # log.txt file has line separated values,
    decks = f.read().split('\n\n')
    for count, deck in enumerate(decks):
        lines = deck.split('\n')
        for x in lines[1:]:
            try:
                mylist[count].append(int(x))
            except ValueError:
                pass

print(mylist)


def combat(deck0, deck1, recurse=True):
    # print("newGame: ", deck0, deck1)
    history = []
    while True:
        if (deck0, deck1) in history:
            # print("Gone Infinite")
            return [1], []
        else:
            history.append((deck0.copy(), deck1.copy()))

        try:
            card0 = deck0.pop(0)
            card1 = deck1.pop(0)
        except IndexError:
            return deck0, deck1
        if recurse and len(deck0) >= card0 and len(deck1) >= card1:
            recdeck0, recdeck1 = combat(deck0[0:card0], deck1[0:card1])
            if len(recdeck0) > len(recdeck1):
                deck0.append(card0)
                deck0.append(card1)
            else:
                deck1.append(card1)
                deck1.append(card0)

        elif card0 > card1:
            deck0.append(card0)
            deck0.append(card1)
        else:
            deck1.append(card1)
            deck1.append(card0)


mylist[0], mylist[1] = combat(mylist[0], mylist[1], recurse=True)

if len(mylist[0]) == 0:
    endDeck = reversed(mylist[1])
else:
    endDeck = reversed(mylist[0])

total = 0
for count, card in enumerate(endDeck):
    total += (1 + count) * card

print(total)
