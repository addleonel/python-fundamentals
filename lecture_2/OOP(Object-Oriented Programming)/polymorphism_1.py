# -*- coding: utf-8 -*-

# I'm going to use la concept POLYMORPHISM
# CONCEPT - POLYMORPHISM
#   > DIFERENTE COMPORTAMIENTO O O IMPLEMENTACION DE UN METHOD  
#     QUE TIENE EL MISMO NOMBRE EN VARIAS CLASES
#   > HABILIDAD QUE TIENEN LOS OBJETOS DE DIFERENTES CLASES PARA RESPONDER
#     A METODOS CON EL MISMO NOMBRE PERO CON IMPLEMENTACION O COMPORTAMIENTo
#     DIFERENTE
# =============================
# FIRST EXAMPLE OF POLYMORPHISM
# WITHOUT INHERITANCE

class Auto:
    wheels = 4
    
    def displacement(self):
        print('It displaces with 4 wheels')

class Moto:
    wheels = 2
    
    def displacement(self):
        print('It displace with 2 wheels')


class Truck:
    wheels = 8
    def displacement(self):
        print('It displace with 8 wheels')

# creating objects
# running without a method
myvehicle = Auto()
myvehicle.displacement() # print 'It displaces with 4 wheels'

myvehicle2 = Moto()
myvehicle2.displacement() # print 'It displace with 2 wheels'

myvehicle3 = Truck()
myvehicle3.displacement() # print 'It displace with 8 wheels'

# running with other way: using a method
myvehicle = Auto()
myvehicle2 = Moto()
myvehicle3 = Truck()

def displace(vehicle):
    # calling the method that is the same in each classes
    vehicle.displacement()
     
displace(myvehicle) # print 'It displaces with 4 wheels'
displace(myvehicle2) # print 'It displace with 2 wheels'
displace(myvehicle3) # print 'It displace with 8 wheels'








