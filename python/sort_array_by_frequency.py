from typing import ItemsView, NamedTuple
from collections import Counter


def frequency_sort(items):
    lst = items 
    zähler = Counter(lst)
    thing = []
    times = []
    for i in lst:
        thing.append(i)
        times.append(zähler[i])
    print(lst)
    print(zähler)
    print(thing)
    print(times)


'''Sort the given iterable so that its elements end up in the decreasing frequency order,
 that is, the number of times they appear in elements. If two elements have the same frequency, 
they should end up in the same order as the first appearance in the iterable. '''

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 1, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")