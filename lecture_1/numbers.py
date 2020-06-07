#Using numbers

#insert a valor
num=input("Insert a number: ")
newNum = int(num) + 23
print(f"your number '{int(num)}' will sum with 23")
print("the sum is: {0} ".format(newNum))
print("...........................................")

num_1 = input("insert the first number: ")
num_2 = input("insert the second number: ")
resultSum = int(num_1)+ int(num_2)
resultRest = int(num_1)- int(num_2)
resultMul = int(num_1)*int(num_2)
resultDiv = int(num_1)/int(num_2)
print(f"the sum of the '{int(num_1)}' and '{int(num_2)}' is: {resultSum}")
print(f"the rest of the '{int(num_1)}' and '{int(num_2)}' is: {resultRest}")
print(f"the multiplication of the '{int(num_1)}' and '{int(num_2)}' is: {resultMul}")
print(f"the division of the '{int(num_1)}' and '{int(num_2)}' is: {resultDiv}")

print(".......................................................")
print("we need numbers that you are going to insert")
print("with the porpuse that calculate the area of circle")
n_1 = input("Insert the value of radio:")
PI = 3.14159265358979
area_circle = PI*(int(n_1)**2)
print("Circle's area is: {0}".format(area_circle))
print(f"When the radio is {int(n_1)} the area of the circle is: {area_circle}")
print("Program finished")
