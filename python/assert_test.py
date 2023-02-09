#insert your shit below,bitch!

def tester(text: str,zahl: int) :
    if str(zahl) in text :
        return "Yay"
    else :
        return "Nay"


if __name__ == "__main__" :

    print(tester("Hallo N1se",1))

    assert tester("bimbo",2) == "Nay"
    assert tester("bambu55",5) == "Yay"
    print("asserts completed")#is only printed if every assert is True,else the code will brak before at the false assertion!

