# I'm going to practice with 'for' statement
# import random
import random


def forStatementFirst():
    # print the elements from a list
    list_first = ['one', 'two', 'three', 'four', 'five']
    for iterator in list_first:
        # iterator take the element value
        # so 'iterator' is equal to, for example, 'one'
        print(iterator, end=", ")
        print("the number of letter: ", str(len(iterator)))


def forStatementSecond():
    list_second = ['one', 'two', 'three', 'four', 'five']
    # print equal to 'forStatementFirst but, with other method
    for iterator in range(len(list_second)):
        print(list_second[iterator], end=", ")
        print("the number of letter: ", len(list_second[iterator]))


def forStatementThird():
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
    print("\r")

def forStatementFourth():
    # exercise with a matrix
    # multiply two matrices using RANDOM NUMBERS
    matrix_1 = [
        # using random numbers
        [random.randint(1, 10), random.randint(-1, 2), random.randint(3, 20)],
        [2, 5, 7],
        [1, 0, 12],

    ]

    matrix_2 = [
        # using random numbers
        [random.randint(1, 10), random.randint(-1, 2), random.randint(3, 20)],
        [2, 5, 7],
        [1, 0, 12],

    ]

    matrix_result = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_1[0])):
                matrix_result[i][j] += matrix_1[i][k]*matrix_2[k][j]

    # print all matrices
    for value in matrix_1:
        print(value)
    print("*")
    for value in matrix_2:
        print(value)
    print("=")
    for value in matrix_result:
        print(value)


# RESULT ABOUT THE METHODS
forStatementFirst()
print("-"*40)
forStatementSecond()
print("-"*40)
forStatementThird()
print("-"*40)
forStatementFourth()

