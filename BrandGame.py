
def brandGame():
    while True:
        print("Type a brand and I will tell you the brand's tradermark")
        print("Which tradermark would you like to see: Nike, Adidas, Puma, Bracelona, Under-Armour")
        brand = input("Tell me a brand: ")
        if "Nike" in brand:
            print("Just do it")
        elif "Adidas" in brand:
            print("Impissible is Nothing")
        elif "Puma" in brand:
            print("The fastest in the world")
        elif "Barcelona" in brand:
            print("mes que un club")
        elif "Under-Armour" in brand:
            print("Protect this house")
        elif brand == 'q':
            break
        else:
            print("Sorry, you might have typed it wrong, or the word typed is not an available option")

brandGame()

    

