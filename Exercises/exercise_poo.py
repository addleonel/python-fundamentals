class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color: {} \nruedas: {}".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        # just when we have one superclass
        # yes in this case, 
        # super(Coche, self).__init__(color, ruedas)
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self)+"\nvelocidad: {} km/h\ncilindrada: {} cc".format(
                                                               self.velocidad,
                                                              self.cilindrada)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self)+ "\ntipo: {}".format(self.tipo)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + "\ncarga: {} kg".format(self.carga)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __srt__(self):
        return Bicicleta.__str__(self) + "\nvelocidad: {} km/h \ncilindrada: {} cc".format(
            self.velocidad,
            self.cilindrada)
    
        
vehiculos = [
    Coche("Green", 4, 200, 1200),
    Camioneta("Red", 4, 300, 2100, 400),
    Bicicleta("Black", 2,"Urbana"),
    Motocicleta("Blue", 2, "Deportiva", 100, 1000),  
]

"""
def catalogar1(list_vehiculos):
    for k in list_vehiculos:
        print(type(k).__name__)
        print(k)
        print()
    # this is optional
    return [type(k).__name__ for k in list_vehiculos]
"""

def catalogar(list_vehiculos, ruedas = None):
    nvehi = 0
    if ruedas != None:
        for k in list_vehiculos:
            if k.ruedas == ruedas:
                print(type(k).__name__)
                print(k)
                print()
                nvehi = nvehi +1
        print(
            "Se han encontrado {} vehiculos con {} ruedas".format(
                                                    nvehi,
                                                  ruedas)
            )
    else:
        for k in list_vehiculos:
            print(type(k).__name__)
            print(k)
            print()

c1 = Coche("red", 4, 200, 1230)
# print(c1)

catalogar(vehiculos)
print("-"*50)
catalogar(vehiculos, 4)
catalogar(vehiculos, 2)
catalogar(vehiculos, 0)




    
        
