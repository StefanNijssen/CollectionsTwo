def addList():
    list = {}
    while True:
        product = input("Wat wilt u toevoegen?")
        if product != "":
            if product in list:
                list[product] += 1
            else:
                list[product] = 1
        else:
            
            return list

def printList(list):
    print("Uw Boodschappenlijstje bestaat uit:")
    for key, value in list.items() :
        print( key, value)
printList((addList()))