# class methods and static methods
# Class method
# Static method

class Student:
    university = "MIT"

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # instance method
    def print_information(self):
        print("Name: {}\nSurname: {} \nage: {}".format(self.name, self.surname, self.age))
        print("University:{}".format(self.university))

    # class method needs '@classmethod' decorator and 'cls' parameter
    @classmethod
    def print_university(cls):
        print("University:{}".format(cls.university))

    # static method needs '@staticmethod' decorator
    @staticmethod
    def print_message(message):
        print(message)


# We need create a instance
student = Student("Alan", "Turing", 23)
student.print_information()

input("press to continuous ...")
# we don't need create a instance when we use class method
# just do this
Student.print_university()
# we don't need create a instance when we use static method
# just do this
input("press to continuous ...")

Student.print_message("Hello, this is a meeting message: ")