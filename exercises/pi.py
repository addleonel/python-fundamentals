import math


def pi_value():
    """
    calculate the pi value using
    sources:
    https://en.wikipedia.org/wiki/Pi
    https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    """
    amount = int(input("type the number of value: "))
    sum = 0
    for k in range(0, amount + 1):
        r = math.pow(-1, k)/(2*k+1)
        sum = sum + r
    print(4*sum)


if __name__ == '__main__':
    pi_value()