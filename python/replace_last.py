#SOLVED
'''Put the last item on the first place in a list. If empty or just one, let it be'''
def replace_last(line): 
    if len(line) <= 1 :
        return line
    else:
        x = line.pop()
        line.insert(0,x)
        return line


if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

