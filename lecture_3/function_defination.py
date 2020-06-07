# I'm going to use functions
# import 'printLine' from 'ifStatement'
from fundamentals.Class_3_MoreControlFlowTools.ifStatement import printLine
import math


# this is a function
def fibonacci(param_NUMBER):
    # in this method i'm going to print fibonacci number
    # using the parameter of the function
    a, b = 0, 1
    while a < param_NUMBER:
        a, b = b, a + b
        print(a, end=" ")


def fibonacci_SECOND(param_NUMBER):
    # fibonacci numbers in a list
    list_FIBONACCI = []
    a, b = 0, 1
    while a < param_NUMBER:
        a, b = b, a + b
        list_FIBONACCI.append(a)
    print(list_FIBONACCI)


# functions using 'math' modules
def solvingMathProblem(number_in_sexagesimal):
    value_x = (math.pi / 180) * number_in_sexagesimal
    function = math.cos(value_x)
    print(function)


def proofmethodMultiply():
    list_PROOF = [1, 1, 0]
    list_RESULT = []
    modules_RESULT = 0
    for i in list_PROOF:
        result_i = i*3
        list_RESULT.append(result_i)
    # module from 'list_RESULT'
    modules_RESULT = math.pow(math.pow(list_RESULT[0], 2)+ math.pow(list_RESULT[1], 2)+math.pow(list_RESULT[2], 2), 0.5)
    print(list_RESULT)
    print(modules_RESULT)

def proofMethodAdd():
    list_PROOF_FIRST = [1, 2, 6]
    list_PROOF_SECOND = [2, -4, 7]
    list_PROOF_THIRD = [1, -3, 4]
    list_PROOF_RESULT = []
    for i in range(len(list_PROOF_FIRST)):
        list_PROOF_RESULT.append(list_PROOF_FIRST[i]+list_PROOF_SECOND[i] + list_PROOF_THIRD[i])

    print(list_PROOF_RESULT)

printLine(30, 0)
fibonacci(10)
printLine(30, 0)
fibonacci_SECOND(20)
printLine(40, 0)
solvingMathProblem(60)
printLine(30, 0)
proofmethodMultiply()
printLine(30, 0)
proofMethodAdd()
