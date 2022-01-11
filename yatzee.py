import random
from collections import Counter

def throwDice(numberOfDice):
    list = []
    min = 1
    max = 5
    for i in range(numberOfDice):
        throw = random.randint(min, max)
        list.append(throw)
    print(list)
    return list
    
def countNumbers(list):
    Total = 0
    print(list)
    while amountOfNumbers > 0:
        positions = int(input("Type in op welke plaats een van de gewenste cijfers staat."))
        listPosition = positions - 1
        Total = Total + (list[listPosition])
        amountOfNumbers = amountOfNumbers - 1
    reroll(list)
    return Total

def reroll(list):
    list2 = []
    roll_Again = input("Wilt u nog een keer?")
    rollAmount = int(input("Hoeveel nummers wilt u rerollen?"))
    if roll_Again == "ja":
        while True:
            rollWichNumbers = int(input("Welk cijfer wilt u houden?"))
            list2.insert(0, list.index(rollWichNumbers))
            throwDice(rollWichNumbers)
            print(list2)
            return list2
    else:
        print("U heeft deze nummers gerollt.")

#random = (throwDice(6))
#print(random)
#amountOfNumbers = int(input("Kies hoeveel cijfers u wilt noteren 1-6\n"))
#print("U mag " + str(amountOfNumbers) + " cijfers kiezen.")

#countNumbers(random)

Dice = throwDice(5)

upper_Half = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']

bottom_Half = ['TOAK', 'FOAK', 'Full_House', 'SmSt', 'LaSt', 'Yatzhee', 'Chance']

half_Choice = input('Wilt u de score in het bovenste of onderste gedeelte invullen?')

if half_Choice == 'bovenste':
    which_Number = int(input('Welk nummer wil je invullen?'))
    amount_Number = Dice.count(which_Number)
    total_Number = amount_Number *(which_Number)
    print(total_Number)
elif half_Choice == 'onderste': 
    which_Combination = input('Welke combinatie wilt u invullen')
    if which_Combination == 'TAOK':
        which_Number = int(input('Welk nummer wil je invullen?'))
        amount_Number = Dice.count(which_Number)
        total_Number = amount_Number *(which_Number)
        if amount_Number >= 3:
            bottom_Half[0] = total_Number
print(bottom_Half)


















# def combinations(list):
#     threeOfaKind = 3
#     if 3 in list == 3:
        
#         print('3')
#     if Counter == 3:
#         #print('3')
#     else:
#          print('2')

#     if len(list) == 3:
#        print("3")

    
# print(combinations(throwDice(3)))
