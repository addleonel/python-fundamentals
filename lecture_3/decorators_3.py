# I'm going ot practice with decorators
import time

def decorator(func):
    def wrap(*args, **kwargs):
        begin = time.time()
        print("="*9)
        position = 1
        s = 0
        for k in func(*args, **kwargs):
            s += k
            print("{} -> {}".format(position, k))
            if position == args[0]:
                print("th sum is: {}".format(s))
                break
            position += 1
        print("="*9)
        end = time.time()
        print("it took: {} {}".format(func.__name__, end-begin))
    return wrap
    
# define function3
@decorator
def fibonacci(to_number):
        a , b = 1, 1
        yield a
        yield b
        while True:
            a = a + b
            b = a + b
            yield a
            yield b


# when to use __name__ == '__main__' ?
# cuando el archivo Python (file.py) es compilada el interprete de Python antes de recorrer cada linea de codigo
# asigna un valor a una varible especial llamada __name__
# el valor que asigne dependera del comportamiento del archivo Python (modulo de Python)
# el comportamiento depende de la importación del archivo Python
# cuando el archivo Python no es importado, la variable __name__ es asignado como '__main__'   
# cuando el archivo Python es importado como modulo a otro modulo, el inperprete de Python asigna a la variable __name__
# como el nombre el modulo ejemplo: si el modulo es llamado file.py entonces __name__ es igual a 'file'.
if __name__ == '__main__':
    m = int(input("type number: "))
    fibonacci(m)
    



