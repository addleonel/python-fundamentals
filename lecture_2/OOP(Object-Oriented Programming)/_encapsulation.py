# PRIVATE WEAK ATTRIBUTES AND METHODS
# USE "_" at the beginning of their name KNOWN AS 'PROTECTED AREA'
# we can access them from a subclass just in the same module
# We cannot access them from another module when importing the class

import math

class Client:
    _code = 2343

class Convert:
    # need an object or instance (self is used)
    def __init__(self):
        # you can use on attributes.
        self._to_radian = math.pi/180
        self._to_grades = 180/math.pi

    def convert_to_radian(self, value):
        value_converted = value*self._to_radian
        self._print_value(value_converted)

    def convert_to_grades(self, value):
        value_converted = value*self._to_grades
        self._print_value(value_converted)

    # you can use on method.
    @staticmethod
    def _print_value(value):
        print(f'Result = {value}')

class Con(Convert):
    pass


if __name__ == '__main__':
    person = Client()
    print(person._code)  # with an object
    print(Client._code)  # with the class

    num = Convert()  # self is the value of the instance
    # need an object
    num.convert_to_radian(30)
    num.convert_to_grades(3.1416)
    # you can access to methods and attributes just with its name
    num._print_value(200)
    print(num._to_radian)
    print(num._to_grades)

    c = Con()
    c._print_value(34)  # you can access methods and attributes from a subclass just in this module
