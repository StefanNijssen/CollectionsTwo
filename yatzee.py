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
def total_value():
    amount_Number = Dice.count(which_Number)
    total_Number = amount_Number *(which_Number)
    return total_Number
Dice = throwDice(5)

upper_Half = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']

bottom_Half = ['TOAK', 'FOAK', 'Full_House', 'SmSt', 'LaSt', 'Yatzhee', 'Chance']

half_Choice = input('Wilt u de score in het bovenste of onderste gedeelte invullen?: ')
if half_Choice == 'bovenste':
    which_Number = int(input('Welk nummer wil je invullen?: '))
    upper_Half[which_Number - 1] = total_value()
    
elif half_Choice == 'onderste':  
    which_Combination = input('Welke combinatie wilt u invullen: ')
    if which_Combination == 'TOAK':
        which_Number = int(input('Welk nummer wil je invullen?: '))
        amount_Number = Dice.count(which_Number)
        if amount_Number >= 3:
            bottom_Half[0] = total_value()
    if which_Combination == 'FOAK':
        which_Number = int(input('Welk nummer wil je invullen?: '))
        amount_Number = Dice.count(which_Number)
        if amount_Number >= 4:
            bottom_Half[1] = total_value()
    if which_Combination == 'FuHo':
        print('Uit welke twee nummers bestaat de Full House?')
        Number1 = int(input('Nummer 1: '))
        Number2 = int(input('Nummer 2: '))
        amount_Number1 = Dice.count(Number1)
        amount_Number2 = Dice.count(Number2)
        if amount_Number1 == 2 and amount_Number2 == 3 or amount_Number1 == 3 and amount_Number2 == 2:
            bottom_Half[2] = 25
    #if which_Combination == 'Chance':
print(upper_Half)
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
