# I'm going to use Inheritance
class Vehicle:
    def __init__(self, price, color):
        self.price = price
        self.color = color
        self.gas = 0

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasleft(self):
        return self.gas


class Truck(Vehicle):
    def __init__(self, price, color, tires):
        super(Truck, self).__init__(price, color)
        self.tires = tires
    

    def beep(self):
        print("honk honk")

class Car(Vehicle):
    def __init__(self, price, color, speed):
        super(Car, self).__init__(price, color)
        self.speed = speed

    def beep(self):
        print("Beep beep")