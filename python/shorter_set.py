#SOLVED!
#  In a given set of integers, you need to remove minimum and maximum elements.

# The second argument tells how many min and max elements should be removed.

# Input: Two arguments. Set of ints and int.

# Output: Set of ints

# Example:
# assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
# assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
# assert remove_min_max({8, 9, 7}, 2) == set()
# assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}

def remove_min_max(data: set, total:int) -> set:
    # your code here
    if total == 0:
        return data
    if len(data) <=(total*2):
        return set()
    
    dato = list(data)

    for i in range(total):
        a = min(dato)
        b = max(dato)
        if len(dato) >= 2:
            dato.remove(a)
            dato.remove(b)
        else:
            return set()
    dati = set(dato)
    return dati
        


print('Example:')
print(remove_min_max({4,5,6,7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()

print("The first mission is done! Click 'Check' to earn cool rewards!")
