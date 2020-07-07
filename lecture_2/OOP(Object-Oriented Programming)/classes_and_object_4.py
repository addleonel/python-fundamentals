# class methods and static methods

import math
class Alumno:
    university = "MIT"

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # instance method
    def printInformation(self):
        print("Name: {}\nSurname: {} \nage: {}".format(self.name, self.surname, self.age))
        print("University:{}".format(self.university))

    @classmethod
    def printUniversity(cls):
        print("University:{}".format(cls.university))

    @staticmethod
    def printAnything(anything):
        print("hello anything: ", anything)


"""
# We need create a instance
alum = Alumno("Alan", "Walker", 23)
alum.printInformation()

input("press to continuous ...")
# we don't need create a instance when we use class method
# just do this
Alumno.printUniversity()
# we don't need create a instance when we use static method
# just do this
input("press to continuous ...")

Alumno.printAnything("this is anything")
"""


class Operations:

    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def rest(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def div(cls, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Don't divide by zero, please try again"

    @staticmethod
    def calculatepi(number):
        sum = 0
        for k in range(1, number+1):
            sum = sum + (math.pow(-1, k+1))/(2*k-1)
        return 4*sum


# the class 'Operation' don't need instance
print(Operations.add(2, 3))

print(Operations.rest(5, 7))

print(Operations.multiply(30, 6))

print(round(Operations.div(12, 13), 3))

print(Operations.multiply(12, 9))

print(Operations.calculatepi(10000))
