
# I'm going to use decorators abilities

def decor(fun):
    def wrap():
        print("-"*30)
        fun()
        print("-"*30)
    return wrap

def print_text():
    print("Tim technologies")

p_text = decor(print_text)
p_text()
# ----------------------------------------------------

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

# ----------------------------------------------------

# if you want to use arguments and key = arguments
print("-"*50)
from datetime import datetime
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
def print_text(arg, list_name = ["Thomas","Charles","Luthor"],
               on={
                    "fname" : "Newton",
                    "sname" : "Copernico",
                    "tname" : "Cooper",
                    "frname" : "Einstein",
                   }):
    print("hello , {}".format(arg))
    print("your friends are:")
    print("-".join(list_name))
    print("your idols are:")
    # using <sep=""> <end="">
    print("{}{}{}{}".format(on["fname"],
                            on["sname"],
                            on["tname"],
                            on["frname"]),sep=" ", end=".")
    
    print(on["fname"],on["sname"],on["tname"],on["frname"],sep="-",end=".")
    
print_text("Marie")

      
    
print(dir({}))
          
    




































    
