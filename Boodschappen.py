def Toevoegen():
    toevoegen = input("Wilt u iets aan het lijstje toevoegen? Y/N")
    if toevoegen == "Y":
        lijstje()
    else:
        print("Uw Boodschappenlijstje bestaat uit:")
        for key, value in list.items() :
            print( key, value)
def lijstje():
    product = input("Wat wilt u toevoegen?")
    if product in list:
        list[product] += 1
    else:
        list[product] = 1
    Toevoegen()
list = {}
Toevoegen()