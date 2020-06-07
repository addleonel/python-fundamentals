# I'm going to use the classes and object


"""
x = 5
y = 'str ng'
z = math.cos(30/math.pi)
print(z)
print(y.replace(' ', 'i'))
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am ", self.name, "and I am ", self.age, "years old")

    def change_age(self, age):
        self.age = age

    def weight(self, we):
        self.we = we


tim = Dog("Tim", 20)
scott = Dog("Scott", 29)

tim.speak()
scott.speak()

tim.change_age(21)

print(tim.age)
tim.speak()
tim.weight(69)
print(tim.we)
scott.weight(70)
print(scott.we)
