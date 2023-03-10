#SOLVED!
def checkio(words: str) -> bool:
    liste = words.rsplit(" ") #rsplit splits the string at the specified separator
    counter = 0
    for word in liste:
        if counter == 3:
            return True
        elif word.isalpha() == True:
            counter += 1
        else :
            counter = 0
    if counter >= 3 :
        return True
    else :
        return False





# #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")




