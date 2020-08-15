
import math

"""
problem 1
    If we list all the natural numbers
    below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
"""
def exercise1():
    m = int(input("type a number:"))
    multiplies = []
    for k in range(m):
        if k % 3 == 0 or k % 5 == 0:
            print(k)
            multiplies.append(k)
    print("the sum of this multiplies of 3 or 5 is: ", math.fsum(multiplies))

exercise1()
