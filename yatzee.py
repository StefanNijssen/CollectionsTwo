import random
from collections import Counter

def throwDice(numberOfDice):
    list = []
    min = 1
    max = 5
    for i in range(numberOfDice):
        throw = random.randint(min, max)
        list.append(throw)
    return list

def total_value():
    amount_Number = Dice.count(which_Number)
    total_Number = amount_Number *(which_Number)
    return total_Number
Dice = throwDice(5)
print(Dice)
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
    if which_Combination == 'ss':
        i = 1
        while i <= 5:
            if i in Dice:
                i = i + 1
                Small = True
            else:
                Small = False
                print('Er is geen Small Straight')
                break
        if Small == True:
            bottom_Half[3] = 30
    if which_Combination == 'ls':
        x = 2
        while x <= 6:
            if x in Dice:
                x = x + 1
                Large = True
            else:
                Large = False
                print('Er is geen Large Straight')
                break
        if Large == True:
            bottom_Half[4] = 40
    if which_Combination == 'Yatzhee':
        which_Number = int(input('Welk nummer wil je invullen?: '))
        amount_Number = Dice.count(which_Number)
        if amount_Number == 5:
            bottom_Half[5] = 50
    if which_Combination == 'Chance':
        bottom_Half[6] = sum(Dice)
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
