"""
Problem 4:
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palindrome_product(number_of_digits):

    nod = number_of_digits
    if nod == 1:
        print('')
    elif nod == 2:
        for i in range(10, 99+1):
            for j in range(10, 99+1):
                if is_palindrome_number(i*j):
                    yield i*j
    elif nod == 3:
        for i in range(100, 999+1):
            for j in range(100, 999+1):
                if is_palindrome_number(i*j):
                    yield i*j
    elif nod <=0 or nod >3:
        print('Don\'t available')

def is_palindrome_number(number):
    if natural_number(number) == reversed_natural_number(number):
        return True
    else:
        return False


def reversed_natural_number(number):
    ln = []
    while number>0:
        r = number%10
        ln.append(r)
        number = number//10
    return ln

def natural_number(number):
    ln = []
    for i in reversed(reversed_natural_number(number)):
        ln.append(i)
    return ln

# problem 4:
# largest_palindrome_product(2)
# print(natural_number(1234))
# print(reversed_natural_number(1234))
# print(is_palindrome_number(90459))
# print(max(list(largest_palindrome_product(3))))
