class Vehiculo:
    """
    base class named Vehiculo
    """
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color: {} \nruedas: {}".\
            format(self.color, self.ruedas)


class Coche(Vehiculo):
    """
    derived class named Coche from Vehiculo
    """
    def __init__(self, color, ruedas, velocidad, cilindrada):
        """
        Just when we have one superclass as in this case, we use
        super(Coche, self).__init__(color, ruedas) instead of
        Vehiculo.__init__(self, color, ruedas)
        """
        super(Coche, self).__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super(Coche, self).__str__() + \
            "\nvelocidad: {} km/h\ncilindrada: {} cc".\
            format(self.velocidad, self.cilindrada)


class Bicicleta(Vehiculo):
    """
    derived class named Bicicleta from Vehiculo
    """
    def __init__(self, color, ruedas, tipo):
        super(Bicicleta, self).__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super(Bicicleta, self).__str__()+ "\ntipo: {}".format(self.tipo)


class Camioneta(Coche):
    """
    Derived class named Camioneta from Coche
    Camioneta -> Coche -> Vehiculo (This behavior is multilevel inheritance)
    """
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super(Camioneta, self).__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super(Camioneta, self).__str__() + "\ncarga: {} kg".format(self.carga)


class Motocicleta(Bicicleta):
    """
    Derived class named Motocicleta from Bicicleta
    Motocicleta -> Bicicleta -> Vehiculo (This behavior is multilevel inheritance)
    """
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super(Motocicleta, self).__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __srt__(self):
        return Bicicleta.__str__() + "\nvelocidad: {} km/h \ncilindrada: {} cc".\
            format(self.velocidad, self.cilindrada)


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
            "Se han encontrado {} vehiculos con {} ruedas".\
            format(nvehi, ruedas)
        )
    else:
        for k in list_vehiculos:
            print(type(k).__name__)
            print(k)
            print()


if __name__ == '__main__':
    c1 = Coche("red", 4, 200, 1230)
    print(c1)

    vehiculos = [
        Coche("Green", 4, 200, 1200),
        Camioneta("Red", 4, 300, 2100, 400),
        Bicicleta("Black", 2, "Urbana"),
        Motocicleta("Blue", 2, "Deportiva", 100, 1000),
    ]

    catalogar(vehiculos)
    print("-"*50)
    catalogar(vehiculos, 4)
    catalogar(vehiculos, 2)
    catalogar(vehiculos, 0)
