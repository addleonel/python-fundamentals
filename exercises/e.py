import math


def e_value():
    """
    calculate the 'e' value
    source:
    https://en.wikipedia.org/wiki/E_(mathematical_constant)
    """
    e = 0
    m = int(input("type the number of values: "))
    for k in range(m):
        e = e + (1/math.factorial(k))
    print(e)


if __name__ == '__main__':
    e_value()
