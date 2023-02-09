#SOLVED
def nearest_value(values: set, one: int) -> int:
    liste = list(values)
    mini = []
    maxi = []
    if one in liste :
        return one
    elif one > max(liste):#THIS was the solution!
        return max(liste)
    elif one < min(liste):#To compare if the given Int is bigger or smaller than anythin inside the liste
        return min(liste)# And return the min or max of the liste if so. Amazing, I fucking LOVE it!
    else:
        for i in liste:
            if i  < one :
                mini.append(i)
            elif i > one:
                maxi.append(i)
                
    if maxi != [] :
        cmax = min(maxi)
    else:
        cmax = None
    if mini != [] : 
        cmin = max(mini)
    else:
        cmin = None
#it fucks if there is nothing bigger/smaller inside  the list
# now how to find wich one is closer?
    dmax = cmax - one
    dmin = one - cmin
    if dmax < dmin:
        return cmax
    else :
        return cmin

if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")