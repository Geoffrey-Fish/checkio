#SOLVED

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    a = ""
    for i in range(len(text)):
        if i == 0:
            a += text[0].upper()
        else :
            a += text[i]    
    if "." not in a :
         a += "."
    return a
if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    #These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
