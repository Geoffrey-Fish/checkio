#task is to sum numbers out of a text but just if the number is not a part of the word
#maybe this time with regex?
import re
def sum_numbers(text: str) -> int:
    # your code here
    text += ' ' ##Here I cheated,because otherwise assert number 3 wouldnt work for whatever reason...
    y = []
    x = re.findall("[0-9]+[^a-zA-Z]", text)
    for i in x:
        y.append(int(i))    
    return sum(y)




if __name__ == '__main__':
    print("Example:")
    print(sum_numbers(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")