# I'm going to use Lambda Functions or lambda expressions
import math
# lambda expression
firstexpression = lambda argument: argument * 2
secondexpression = lambda base, altura: (base * altura) / 2
thirdexpression1 = lambda seconds: "Equivale a {0} minutos".format(seconds / 60)
thirdexpression2 = lambda seconds: "Equivale a " + str(seconds / 60) + " minutos o " + str(seconds / 3600) + " horas"


# lambda expression as anonymous function
def lambdaFunction_ONE(a, b, c):
    sum = a + b + c
    if sum < 0:
        print("the result", sum, "is negative")
        return lambda x: "The sum " + str(sum) + " multiply by " + str(x) + " is: " + str(x * sum)
    else:
        print("the result", sum, "is positive")
        return lambda x: "The sum " + str(sum) + " multiply by " + str(x) + " is: " + str(x * sum)


# validation
def validation_INT(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("just integer number")

def validation_NUMBER(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Just number, try again")

def sumofnumber():
    lst = []
    sum = 0
    quantity = validation_INT("quantity of number: ")
    for i in range(quantity):
        number = validation_NUMBER("type a number: ")
        lst.append(number)
    # sum of a list
    sum = math.fsum(lst)
    print("the sum is: ", sum)
    return lambda x: math.sqrt(sum)*x
    


# RESULT
print(firstexpression(12))
print(secondexpression(12, 2))
print(thirdexpression1(3600))
print(thirdexpression2(100))
print("-----------------------")
funtionlambda = lambdaFunction_ONE(-1, -3, -4)
print(funtionlambda(20))
print("-"*30)
suma = sumofnumber()
print(suma(10))

