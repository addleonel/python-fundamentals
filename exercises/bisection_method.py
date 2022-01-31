import math


def bisection_method(x_a, x_b):
    """
    T'm going to find a root of a function using the bisection method
    x_a and x_b are intervals
    """
    i = 0
    x_r_before = 0
    while True:
        f_a = function(x_a)
        x_r = (x_a+x_b)/2
        f_r = function(x_r)
        print('the value N°', i, ':', x_r)

        if i > 0:
            error = math.fabs((x_r - x_r_before) / x_r)*100
            if error == 0:
                print('the answer is:', x_r)
                break

        sig = f_a * f_r
        if sig > 0:
            x_a = x_r
        elif sig < 0:
            x_b = x_r
        x_r_before = x_r
        i = i + 1


def function(x):
    # f = math.pow(x, 10)-1
    # f = 4959.737 * math.pow(x, 1.418) - 1165.217 * math.pow(x, 1.709) - 4669.88
    # f = 5*math.pow(x,8)+7*math.pow(x,7)-4*math.pow(x,6)+17*math.pow(x,5)-19*math.pow(x,4)+11*math.pow(x,3)-15*math.pow(x,2)+25*x+11
    # print(f)
    return math.pow(x, 3)-x -2


if __name__ == '__main__':
    # bisection_method(-3, -2)
    print("-"*30)
    # bisection_method(-0.5, 0)
    bisection_method(1, 2)
