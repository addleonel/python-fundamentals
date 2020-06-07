# METODOS Y TRIBUTOS FUERTEMENTE PRIVADOS UTILIZAN "__" al inicio de su nombre
# CONOCIDO 'AMBITO PRIVADO'
import math

class Client:
    __codigo = 4565
    

person = Client()
print(person._Client__codigo) # Así es como se debe acceder al atributo privado 

# ---------------------------------------------------------------------

class Convert:
    
    # -----------------------------------------------
    # NECESITA DE UN OBJETO O INSTANCIAR (SE UTILIZA self)
    
    def __init__(self):
        self.__to_radian = math.pi/180
        self.__to_sexage = 180/math.pi
        
    def convert_to_radian(self, value):
        value_converted = value*self.__to_radian
        self.__printvalue(value_converted)
        
    def convert_to_sexage(self, value):
        value_converted = value*self.__to_sexage
        self.__printvalue(value_converted)
    
    def __printvalue(self, value):
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
print(num._Convert__to_radian)
# no necesita de un objeto
Convert.add(2, 5)









#print(person.__codigo) # no se puede acceder de esta manera



