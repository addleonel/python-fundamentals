# I'm going to practice with 'for' statement
# import random
import random


def forStatement_FIRST():
    # print the elements from a list
    list_FIRST = ['one', 'two', 'three', 'four', 'five']
    for iterator in list_FIRST:
        # iterator take the element value
        # so 'iterator' is equal to, for example, 'one'
        print(iterator, end=", ")
        print("the number of letter: ", str(len(iterator)))


def forStatement_SECOND():
    list_SECOND = ['one', 'two', 'three', 'four', 'five']
    # print equal to 'forStatement_FIRST but, with other method
    for iterator in range(len(list_SECOND)):
        print(list_SECOND[iterator], end=", ")
        print("the number of letter: ", len(list_SECOND[iterator]))


def forStatement_THIRD():
    # I'm going to print ranges
    for i in range(2, 20, 4):
        print(i, end=" ")
    print()
    for i in range(1, 10, 3):
        print(i, end=" ")
    print()
    for i in range(20, 68, 10):
        print(i, end=" ")
    print()
    for i in range(30, 12, -5):
        print(i, end=" ")
    print()
    for i in range(-10, 20, 5):
        print(i, end=" ")
    print()
    for i in range(-10, -100, -10):
        print(i, end=" ")
    # Make a list with ranges
    # for example
    print()
    list_WITH_RANGE_FIRST= list(range(12, 28, 2))
    print(list_WITH_RANGE_FIRST)
    list_WITH_RANGE_SECOND = list(range(20, 40, 7))
    print(list_WITH_RANGE_SECOND)
    list_WITH_RANGE_THIRD = list(range(1,10+1))
    print(list_WITH_RANGE_THIRD)

def forStatement_FOURTH():
    # exercise with a matrix
    # multiply two matrices using RANDOM NUMBERS
    matrix_FIRST = [
        # using random numbers
        [random.randint(1, 10), random.randint(-1, 2), random.randint(3, 20)],
        [2, 5, 7],
        [1, 0, 12],

    ]

    matrix_SECOND = [
        # using random numbers
        [random.randint(1, 10), random.randint(-1, 2), random.randint(3, 20)],
        [2, 5, 7],
        [1, 0, 12],

    ]

    matrix_RESULT = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    for i in range(len(matrix_FIRST)):
        for j in range(len(matrix_SECOND[0])):
            for k in range(len(matrix_FIRST[0])):
                matrix_RESULT[i][j] += matrix_FIRST[i][k]*matrix_SECOND[k][j]

    # print all matrices
    for value in matrix_FIRST:
        print(value)
    print("*")
    for value in matrix_SECOND:
        print(value)
    print("=")
    for value in matrix_RESULT:
        print(value)


# METHODS COMPLEMENTS
def proofMethod():
    list_PROOF = ['one', 'two', 'three', 'four', 'five']
    for iterator in range(len(list_PROOF)):
        print(list_PROOF[iterator])
    # for i in range(10):
    #    print(i)


def printLine():
    print("--------------------------------------------------")


# RESULT ABOUT THE METHODS

forStatement_FIRST()
printLine()
forStatement_SECOND()
printLine()
forStatement_THIRD()
printLine()
forStatement_FOURTH()
# proofMethod()
