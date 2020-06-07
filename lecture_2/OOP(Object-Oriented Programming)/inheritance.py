# this is a superclass
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.encendido = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frenar = True

    def show_feautures(self):
        print("Marca: {} \nModelo: {}".format(self.marca, self.modelo))


# this is a subclass
class Velectricos(Vehiculo):
    def __init__(self, marca, modelo, bateria, fuente_de_energia):
        super(Velectricos, self).__init__(marca, modelo)
        self.bateria = bateria
        self.fuente_de_energia = fuente_de_energia
        self.cargar = False

    def cargarenergia(self):
        self.cargar = True

    # overrides of  'show_feautures' from 'Vehiculo' class
    def show_feautures(self):
        print("Marca: {} \nModelo: {} \nBateria: {} \nFuente: {}".format(self.marca,
                                                                         self.modelo,
                                                                         self.bateria,

                                                                       self.fuente_de_energia))

class Vvapor(Vehiculo):
    def __init__(self, marca, modelo, our_description):
        super(Vvapor, self).__init__(marca, modelo)
        self.our_description = our_description

    def show_feautures(self):
        print("Marca: {} \nModelo: {} \nDescription: {}".format(self.marca,
                                                                self.modelo,
                                                                self.our_description))



# this is other subclass
class Bicielectrica(Velectricos, Vehiculo): # preferencia para 'Velectricos'
    def __init__(self, marca, modelo, bateria, fuente_de_energia, ruedas):
        super(Bicielectrica, self).__init__(marca, modelo, bateria, fuente_de_energia)
        self.ruedas = ruedas

    def show_feautures(self):
        print("Marca: {} \nModelo: {} \nBateria: {} \nFuente: {} \nRuedas: {}".format(self.marca,
                                                                         self.modelo,
                                                                         self.bateria,
                                                                         self.fuente_de_energia,
                                                                         self.ruedas))




# out of the class
# create a instance
my_car_1 = Vehiculo("Auri", "XM-23")
my_car_1.show_feautures()
print("-" * 40)
my_car_2 = Vehiculo("Ferrari", "XVM-34")
my_car_2.show_feautures()
print("-" * 40)
my_car_3 = Vehiculo("Toyota", "506-D")
my_car_3.show_feautures()
print("-"*40)
my_car_4 = Velectricos("Hyuntai", "34-M", "litio", "recargable")
my_car_4.show_feautures()
print("-"*40)
my_car_5 = Bicielectrica("suzuki", "MN-567", "Litio", "Recargable", 4)
my_car_5.show_feautures()
