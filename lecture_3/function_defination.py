# I'm going to use functions

import math


# this is a function
def fibonacci(param_number):
    # in this method i'm going to print fibonacci number
    # using the parameter of the function
    a, b = 0, 1
    while a < param_number:
        a, b = b, a + b
        print(a, end=" ")


def fibonacci_second(param_number):
    # fibonacci numbers in a list
    list_fibonacci = []
    a, b = 0, 1
    while a < param_number:
        a, b = b, a + b
        list_fibonacci.append(a)
    print(list_fibonacci)


# functions using 'math' modules
def solvingMathProblem(number_in_sexagesimal):
    value_x = (math.pi / 180) * number_in_sexagesimal
    function = math.cos(value_x)
    print(function)


def proofMethodMultiply():
    list_proof = [1, 1, 0]
    list_result = []
    modules_result = 0
    for i in list_proof:
        result_i = i*3
        list_result.append(result_i)
    # module from 'list_result'
    modules_result = math.pow(math.pow(list_result[0], 2)+math.pow(list_result[1], 2)+math.pow(list_result[2], 2), 0.5)
    print(list_result)
    print(modules_result)

def proofMethodAdd():
    list_proof_first = [1, 2, 6]
    list_proof_second = [2, -4, 7]
    list_proof_third = [1, -3, 4]
    list_proof_result = []
    for i in range(len(list_proof_first)):
        list_proof_result.append(list_proof_first[i]+list_proof_second[i] + list_proof_third[i])

    print(list_proof_result)


print("-"*30)
fibonacci(10)
print("-"*30)
fibonacci_second(20)
print("-"*40)
solvingMathProblem(60)
print("-"*30)
proofMethodMultiply()
print("-"*30)
proofMethodAdd()
