import random
def Namen():
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
                print(listNamen)
            break

def randomLootje(listNamen):
    list = []
    throw = random.randint(min, max)
    return list
Namen()