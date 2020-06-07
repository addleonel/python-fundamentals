import math
"""
problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def pythagorean_tripet(big_number):
    for a in range(1,big_number+1):
        for b in range(1, a+1):
            c = math.sqrt(a**2 + b**2)
            sc = a + b + c
            if sc == 1000:
                p = a*b*c
                print('a = {}, b = {}, c = {}\nsum = {}, product = {}'.format(a,
                                                                              b,
                                                                              c,
                                                                              sc,
                                                                              p))
                break


# problem 9:
pythagorean_tripet(1000)
