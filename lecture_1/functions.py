#using funcions
def sumwithinput():
    num1=int(input("first number: "))
    num2=int(input("second number: "))
    suma=num1+num2
    return suma
def printTheSum(number):
    if number%2 ==0:
        print("result : ",number)
        print("it's pair")
    else:
        print("result : ",number)
        print("it's odd")

numero= sumwithinput()
printTheSum(numero)
print(type(sumwithinput()))

