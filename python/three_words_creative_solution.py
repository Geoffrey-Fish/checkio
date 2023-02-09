import re

def checkio(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    '''Took me a while to get what '\D+\s\D+\s\D+' meant, to other readers:

\D = any non-digit character.

The + makes \D work on words.

\s = any whitespace.

Read more here: https://docs.python.org/3/library/re.html
'''