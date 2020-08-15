# In this module I'm going to solve the bisection method

import math

# x_a and x_b are intervals

def fpMETHOD(x_a, x_b):
    i = 0
    x_r_before = 0
    while True:
        f_a = function(x_a)
        f_b = function(x_b)
        REST = x_b - x_a
        x_r = x_b - (f_b * REST / (f_b - f_a))
        f_r = function(x_r)
        print("the value N°", i, ":", x_r)

        if i > 0:
            ERROR = math.fabs((x_r - x_r_before) / x_r)
            if ERROR == 0:
                print("the answer is:", x_r)
                break

        sig = f_a * f_r
        if sig > 0:
            x_a = x_r
        elif sig < 0:
            x_b = x_r
        x_r_before = x_r
        i = i + 1


def function(x):
    f = (math.pi * (1 - math.exp(-x)) / x) - 0.5
    # print(f)
    return f


# RESULT
fpMETHOD(5, 7)
