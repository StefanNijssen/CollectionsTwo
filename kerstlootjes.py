import random
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


def randomLootje(list):
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
randomLootje(vraagNamen()) 