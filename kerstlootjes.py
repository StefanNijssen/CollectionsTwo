import random
from typing import List
def vraagNamen():
    listNamen = []
    while True:
        Naam = input("Voer een unieke naam in.")
        if Naam != "":
            if Naam in listNamen:
                print("Deze naam is al opgegeven. Voer een nieuwe naam in.")
            else:    
                listNamen.append(Naam)
        else:
            if len(listNamen) >= 2:
                return listNamen
            break


def randomLootjee(list):
    list = []
    dict = {}
    dict = list
    
    while len(dict) > 0:
        personTicket = random.choice(list)
        dict.add(personTicket)
        list.remove(personTicket)
        for i in range(1, len(list)):
            for key,val in dict.items():
                if key in dict:
                    dict[key] = [dict[key],val]
            
    return list

def randomLootje(list):
    listA = list[:]
    listB = list[:]

    random.shuffle(listA)
    random.shuffle(listB)
    dict = {}

    for index in range(min(len(listA),len(listB))):

        dict[listA[index]] = listB[index]
    print(dict)

randomLootje(vraagNamen()) 