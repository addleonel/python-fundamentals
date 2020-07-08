
# CONCEPT - POLYMORPHISM
# > DIFFERENT BEHAVIOR OR OR IMPLEMENTATION OF A METHOD
# THAT HAS THE SAME NAME IN SEVERAL CLASSES
# > SKILLS THAT OBJECTS OF DIFFERENT CLASSES HAVE TO RESPOND
# A METHODS WITH THE SAME NAME BUT WITH IMPLEMENTATION OR BEHAVIOR
# DIFFERENT
# =============================
# FIRST EXAMPLE OF POLYMORPHISM
# WITHOUT INHERITANCE

class Car:
    wheels = 4

    @staticmethod
    def displacement():
        print('It displaces with 4 wheels')


class Motorcycle:
    wheels = 2

    @staticmethod
    def displacement():
        print('It displace with 2 wheels')


class Truck:
    wheels = 8

    @staticmethod
    def displacement():
        print('It displace with 8 wheels')


# creating objects
# running without a method
myvehicle = Car()
myvehicle.displacement()  # print 'It displaces with 4 wheels'

myvehicle2 = Motorcycle()
myvehicle2.displacement()  # print 'It displace with 2 wheels'

myvehicle3 = Truck()
myvehicle3.displacement()  # print 'It displace with 8 wheels'

# running with other way: using a method
myvehicle = Car()
myvehicle2 = Motorcycle()
myvehicle3 = Truck()

def displace(vehicle):
    # calling the method that is the same in each classes
    vehicle.displacement()


displace(myvehicle)  # print 'It displaces with 4 wheels'
displace(myvehicle2)  # print 'It displace with 2 wheels'
displace(myvehicle3)  # print 'It displace with 8 wheels'








