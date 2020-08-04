# using funcions
def sumWithInput():
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    sum_ = num1 + num2
    return sum_


def printTheSum(number):
    if number % 2 == 0:
        print("result : ", number)
        print("it's pair")
    else:
        print("result : ", number)
        print("it's odd")


number_ = sumWithInput()
printTheSum(number_)
print(type(sumWithInput()))

