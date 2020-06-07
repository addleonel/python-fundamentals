# I'm going to solve the root of a function using Newton-Raphson Method

# import modules
import math


def runMethod(x_i):
    iterator = 0
    while True:
        f = function_ORIGINAL(x_i)
        f_d = function_DERIVED(x_i)
        x_next = x_i - (f / f_d)
        print("the value N°", iterator, ":", x_next)
        ERROR = math.fabs((x_next - x_i) / x_next) * 100
        if ERROR == 0:
            print("the answer:", x_next)
            break
        x_i = x_next
        iterator = iterator + 1

def function_ORIGINAL(x):
    # f = 2 * math.sin(x) - x
    f = 50*math.pow(x, 2)-31.266274*x+0.004248
    return f


def function_DERIVED(x):
    # f_derived = 2 * math.cos(x) - 1
    f_derived = 100*x-31.266274
    return f_derived


# RESULT
# runMethod(1)
runMethod(20)
print("-"*30)
runMethod(-20)
