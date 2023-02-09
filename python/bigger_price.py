def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code
    
    liste = []
    for i in data:
        liste.append(i['price'])
    maxi = max(liste)
    ind = liste.index(maxi)
    # if limit > 1:
    #     clone = data
    #     clone.pop()
    #     cloneliste = []
    #     for i in clone:
    #         cloneliste.append(i['price'])
    #         clonemaxi = max(cloneliste)
    #         cloneind = cloneliste.index(clonemaxi)
    #print(clone)
    if limit > 1:
        print(data[ind],clone[cloneind])
    print(data[ind])

if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # # These "asserts" using for self-checking and not for auto-testing
    # assert bigger_price(2, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]) == [
    #     {"name": "wine", "price": 138},
    #     {"name": "bread", "price": 100}
    # ], "First"

    # assert bigger_price(1, [
    #     {"name": "pen", "price": 5},
    #     {"name": "whiteboard", "price": 170}
    # ]) == [{"name": "whiteboard", "price": 170}], "Second"

    # print('Done! Looks like it is fine. Go and check it')
