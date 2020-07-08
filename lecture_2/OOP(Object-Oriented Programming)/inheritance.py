
# INHERITANCE

# this is a superclass
class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
        self.switched_on = False
        self.accelerate = False
        self.slow_down = False

    def start_the_car(self):
        self.switched_on = True

    def speed_up(self):
        self.accelerate = True

    def slow_down_car(self):
        self.slow_down = True

    def show_features(self):
        print("mark: {} \nmodel: {}".format(self.mark, self.model))


# this is a subclass
class Electrical(Vehicle):
    def __init__(self, mark, model, battery, power_source):
        super(Electrical, self).__init__(mark, model)
        self.battery = battery
        self.power_source = power_source
        self.load = False

    def load_energy(self):
        self.load = True

    # overrides of  'show_features' from 'Vehicle' class
    def show_features(self):
        print("mark: {} \nmodel: {} \nbattery: {} \nSource: {}".format(self.mark,
                                                                       self.model,
                                                                       self.battery,
                                                                       self.power_source))
# this is other subclass
class Steam(Vehicle):
    def __init__(self, mark, model, our_description):
        super(Steam, self).__init__(mark, model)
        self.our_description = our_description

    def show_features(self):
        print("mark: {} \nmodel: {} \nDescription: {}".format(self.mark,
                                                              self.model,
                                                              self.our_description))


# We are going to create a multiple inheritances
# this is other subclass
class ElectricBike(Electrical, Vehicle):  # preference for 'Electrical'
    def __init__(self, mark, model, battery, power_source, wheels):
        super(ElectricBike, self).__init__(mark, model, battery, power_source)
        self.wheels = wheels

    def show_features(self):
        print("mark: {} \nmodel: {} \nbattery: {} \nSource: {} \nwheels: {}".format(self.mark,
                                                                                    self.model,
                                                                                    self.battery,
                                                                                    self.power_source,
                                                                                    self.wheels))


# out of the class
# create a instance
my_car_1 = Vehicle("Audi", "XM-23")
my_car_1.show_features()

print("-" * 40)

my_car_2 = Vehicle("Ferrari", "XVM-34")
my_car_2.show_features()

print("-" * 40)

my_car_3 = Vehicle("Toyota", "506-D")
my_car_3.show_features()

print("-"*40)

my_car_4 = Electrical("Hyundai", "34-M", "Lithium", "rechargeable")
my_car_4.show_features()

print("-"*40)

my_car_5 = ElectricBike("suzuki", "MN-567", "Lithium", "rechargeable", 4)
my_car_5.show_features()
