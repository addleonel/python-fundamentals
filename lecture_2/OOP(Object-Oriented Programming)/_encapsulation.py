# METODOS Y TRIBUTOS DÉBILES PRIVADOS UTILIZAN "_" al inico de su nombre
# CONOCIDO COMO 'AMBITO PROTEGIDO'
#
#
import math

class Client:
    _codigo = 2343
    


person = Client()

print(person._codigo)
print(Client._codigo)


# ---------------------------------------------------------------------

class Convert:
    
    # -----------------------------------------------
    # NECESITA DE UN OBJETO O INSTANCIAR (SE UTILIZA self)
    
    def __init__(self):
        self._to_radian = math.pi/180
        self._to_sexage = 180/math.pi
        
    def convert_to_radian(self, value):
        value_converted = value*self._to_radian
        self._printvalue(value_converted)
        
    def convert_to_sexage(self, value):
        value_converted = value*self._to_sexage
        self._printvalue(value_converted)
    
    def _printvalue(self, value):
        print("Result = {}".format(value))
    # ----------------------------------------------    
        
    # ----------------------------------------------
    # NO REQUIERE DE UN OBJETO O INSTANCIA (NO UTILIZA self)
    
    def add(x, y):
        print(x + y)
        
    # ----------------------------------------------

num = Convert() # self es el valor de la instancia
# necesita de un objeto
num.convert_to_radian(30)
num.convert_to_sexage(3.1416)
num._printvalue(200)
print(num._to_radian)
print(num._to_sexage)

# no necesita de un objeto
Convert.add(2, 5)

