
# STRONGLY PRIVATE METHODS AND ATTRIBUTES USE "__" at the beginning of their name
# KNOWN 'PRIVATE FIELD'
# Private methods are those methods that should neither be accessed outside the class nor by any base class.

import math

class Client:
    __code = 4565

class Convert:

    def __init__(self):
        # you can use on attributes.
        self.__to_radian = math.pi/180
        self.__to_grades = 180/math.pi

    def convert_to_radian(self, value):
        value_converted = value*self.__to_radian
        return value_converted
        
    def convert_to_grades(self, value):
        value_converted = value*self.__to_grades
        return value_converted

    # Also you can use on methods.
    def __value_message(self):
        return "The values are radian convert = {} and grades convert = {}".format(self.__to_radian, self.__to_grades)

    def print_value_message(self):
        print(self.__value_message())


if __name__ == '__main__':
    person = Client()
    # print(person.__code)  # returns AttributeError: 'Client' object has no attribute '__code'
    print(person._Client__code)  # This is how the private attribute should be accessed

    num = Convert()  # self is the value of the instance
    print(num.convert_to_radian(30))
    print(num.convert_to_grades(1.45))
    num.print_value_message()
    # print(num.__value_message())  # returns AttributeError: 'Convert' object has no attribute '__value_message'
    print(num._Convert__value_message())  # This is how the private method should be accessed