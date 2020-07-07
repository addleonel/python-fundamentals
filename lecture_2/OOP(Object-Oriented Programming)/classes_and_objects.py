# classes and object

class Person:

    # constructor method
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.we = weight

    # instance methods (they have 'self' parameter)
    # they are accessed from an object or instance
    def speak(self):
        print("I am", self.name, ", I am ", self.age, "years old, and my weight is", self.we)

    def change_age(self, age):
        self.age = age

    def change_weight(self, we):
        self.we = we


tim = Person("Tim", 21, 1.75)  # tim is an object or instance
scott = Person("Scott", 29, 1.80)  # scott is other object or instance

# calling to the instance method
tim.speak()
tim.change_age(23)
tim.change_weight(1.77)
tim.speak()

scott.speak()
scott.change_age(30)
scott.change_weight(1.81)
scott.speak()

