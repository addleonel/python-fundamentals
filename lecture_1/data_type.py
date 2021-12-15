# Data Type
if __name__ == '__main__':

    # Text Type: string (str)
    # string
    print("My title")
    print(type('this a string'))  # str, This is a string

    # Numeric Types: integer (int), float, complex
    # integer
    print(100)
    print(type(100))  # int, This is a integer
    # float
    print(20.3)
    print(type(20.35))  # float, This is a float
    # complex
    print(4 + 3j)
    print(type(3 + 4j))  # complex

    # Boolean Type: bool
    print(True)
    print(type(False))  # bool, This is a boolean
 
    # Sequence Types: list, tuple, range
    # list
    print([12, 11, 35, 56, 24])
    print(type([12, "book", True, 20.3]))  # list, This is a list
    # tuples
    print((12, 23, 34, 565))
    print(type(()))  # tuple, This is a empty tuple
    # range
    print(range(20))
    print(type(range(1, 10, 2)))  # range, This is range

    # Mapping Type: dictionary (dict)
    # dictionary
    print({
        "name": "Albert",
        "surname": "Einstein",
        "age": 20
    })
    print(type({
        "name": "Albert",
        "surname":  "Einstein",
        "age": 20
    }))  # dict, This is a dictionary

    # Set Types: set, frozenset (immutable set)
    # set
    print({4, 3, 2, 7})
    print(type({56, 12, 34}))  # set, This is a set
    # frozenset
    print(frozenset([3, 4, 5, 6]))
    print(type(frozenset({2, 2, 3, 3, 1})))  # frozenset, This is a frozenset



