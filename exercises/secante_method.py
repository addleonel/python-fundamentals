# I'm going to solve a function using secant method
import math


def secant_METHOD(x_i, x_i_1):
    iterator = 0
    while True:
        f_i = function(x_i)
        f_i_1 = function(x_i_1)
        Rest = x_i - x_i_1
        x_next = x_i - ((f_i * Rest) / (f_i - f_i_1))
        print("the value N°", iterator, ":", x_next)
        ERROR = math.fabs((x_next - x_i) / x_next)*100
        if ERROR == 0:
            print("the answer: ", x_next)
            break
        x_i_1 = x_i
        x_i = x_next
        iterator = iterator + 1


def function(x):
    f = math.exp(-x) - x
    return f


if __name__ == '__main__':
    # RESULT
    secant_METHOD(2, 5)
