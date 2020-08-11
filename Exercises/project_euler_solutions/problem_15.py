"""
problem 15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def routes_to(rows):
    return factorial(2*rows)/(factorial(rows)*factorial(rows))


def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num-1)


# print(factorial(5))
print(routes_to(20))