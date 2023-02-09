#SOLVED
def checkio(array: list) -> int:
    if len(array) == 0 :
        return 0
    elif len(array) == 1 :
        return array[0]*array[0]
    else :
        calc = []
        for num in range(0,len(array)):
            if num %2 == 0:
                calc.append(array[num])
        return sum(calc) * array[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    assert checkio([-89,-86,13,-69,94,-75,66,97,-50]) == -1700, "Yeah,Bitch, try again!"
    assert checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]) == 1968, "now there is that fuckery.fuck."
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
