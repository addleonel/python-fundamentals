# a function 'a' receives as a parameter a function 'b' and returns a function 'c'
# a(b) ->c
# 'a' is the decorator
# 'b' function to decorate
# 'c' decor 'b'
import time

def function_a(func):

    def function_c(*args, **kwargs):
        return func(*args, **kwargs)

    return function_c

@function_a
def function_b(value1, value2, value3):
    pass
# run function decorated
# function_b()

def decorator(func):
    
    def wrap(*args, **kwargs):
        start = time.time()
        print(func(*args, **kwargs))
        return time.time()-start
        
    return wrap


@decorator
def sum_(a, b):
    # time.sleep(3)
    return a + b


value_returned = sum_(2,3)  # time.time()-start = wrap
print(value_returned)








