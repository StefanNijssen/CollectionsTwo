import itertools, random

deck = list(itertools.product(range(1,15),['Schoppen','Harten','Ruiten','Klaver']))
random.shuffle(deck)

for i in range(7):
    if deck[i][0] == 11:
        print(deck[i][1] + " Boer")
    elif deck[i][0] == 12:
        print(deck[i][1] + " Vrouw")
    elif deck[i][0] == 13:
        print(deck[i][1] + " Koning")
    elif deck[i][0] == 14:
        print(deck[i][1] + " Aas")
    else:
        print(deck[i][1], deck[i][0])
