# I'm going to use Polymorphism


class Vehicle:
    """
    base class called Vehicle
    """
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
    """
    derived class named Truck
    """
    def __init__(self, price, color, tires):
        super(Truck, self).__init__(price, color)
        self.tires = tires

    def beep(self):
        print("honk honk")


class Car(Vehicle):
    """
    Derived class named Car
    """
    def __init__(self, price, color, speed):
        super(Car, self).__init__(price, color)
        self.speed = speed

    def beep(self):
        print("Beep beep")


def do_beep(vehicle):
    """
    function to call beep method
    """
    vehicle.beep()


if __name__ == '__main__':
    truck1 = Truck('2000', 'red', 'some')
    car1 = Car('4000', 'blue', 'some')
    do_beep(truck1)
    do_beep(car1)
