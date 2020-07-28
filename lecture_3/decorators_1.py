# DECORATORS
# I'm going to use decorators abilities
from datetime import datetime  # this is for an example below

def decor(fun):
    def wrap():
        print("-"*30)
        fun()
        print("-"*30)
    return wrap

def print_text():
    print("Leonel technologies")


p_text = decor(print_text)
p_text()

# Other form with the same example
print("-"*50)
print()
def decor2(fun):
    def wrap():
        print("-"*30)
        fun()
        print("-"*30)
    return wrap

@decor2
def print_text2():
    print("Heron Dynamics")


print_text2()


# if you want to use arguments and key = arguments
print("-"*50)
def decorator(func):
    def wrap(*args, **kwargs):
        print("-"*30)
        if 7 <= datetime.now().hour < 24:
            func(*args, **kwargs)
        else:
            print("hello, everyone")
        print()
        print("-"*30)

    return wrap


@decorator
def print_text(name, *args, **kwargs):
    print("hello , {}".format(name))
    print("your friends are:")
    for k in args:
        print(k, end=',')
    print('\r')
    print("your idols are:")
    # using sep="" and end="" parameters
    print(kwargs["fname"], kwargs["sname"], kwargs["tname"], sep=", ", end=".")


print_text('Marie', 'Michael', 'Albert', 'Tom', fname='Linus Torvalds', sname='Dennis Ritchie', tname='Alan Turing')
          
    




































    
