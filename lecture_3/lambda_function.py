# I'm going to use Lambda Functions or Lambda Expressions

import math

# lambda expression

first_expression = (lambda argument: argument * 2)
second_expression = (lambda base, height: (base * height) / 2)
third_expression1 = (lambda seconds: "It's equivalent {0} minutes".format(seconds / 60))
third_expression2 = (lambda seconds: "It's equivalent to " +
                                     str(seconds / 60) + " minutes or " + str(seconds / 3600) + " hours")


# lambda expression as anonymous function
def signOfTheSum(a, b, c):
    sum_ = a + b + c
    if sum_ < 0:
        print("the result", sum_, "is negative")
        return lambda x: "The sum " + str(sum_) + " multiplied by " + str(x) + " is: " + str(x * sum_)
    else:
        print("the result", sum_, "is positive")
        return lambda x: "The sum " + str(sum_) + " multiplied by " + str(x) + " is: " + str(x * sum_)


# validation
def validation_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("just integer number")

def validation_float(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Just number, try again")

def sumOfNumber():
    lst = []
    sum = 0
    quantity = validation_int("quantity of number: ")
    for i in range(quantity):
        number = validation_float("type a number: ")
        lst.append(number)
    # sum of a list
    sum = math.fsum(lst)
    print("the sum is: ", sum)
    return lambda x: math.sqrt(sum)*x


# RESULT
print(first_expression(12))
print(second_expression(12, 2))
print(third_expression1(3600))
print(third_expression2(100))
print("-"*40)
function_lambda = signOfTheSum(-1, -3, -4)
print(function_lambda(20))
print("-"*30)
sum_to = sumOfNumber()
print(sum_to(10))
print("-"*40)
sign = (lambda x, y: x+y)
print(sign(2, 3))



