# una funcion 'a' recibe como parametro una funcion 'b' y retorna una funcion 'c'  
#a(b) ->c
# 'a' is the decorator
# 'b' function to decorate (funcion para decorar)
# 'c' decora 'b'
# -------------------------------------------------
def function_a(function_b):

    def function_c(*args, **kwargs):
        return function_b(*args, **kwargs)

    return function_c

@function_a
def function_b(value1, value2, value3):
    pass
# run function decorated
# function_b()
# --------------------------------------------------
import time
def decorator(func):
    
    def wrap(*args, **kwargs):
        start = time.time()
        print(func(*args, **kwargs))
        return time.time()-start
        
    return wrap

@decorator
def sum(a, b):
    #time.sleep(3)
    return a + b
value_returned = sum(2,3) # time.time()-start = wrap
print(value_returned)

# ------------------------------------------------------------








