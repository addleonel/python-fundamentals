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
    a, b = 1, 1
    yield a
    yield b
    while True:
        a = a + b
        b = a + b
        yield a
        yield b


if __name__ == '__main__':
    fibonacci(30)
