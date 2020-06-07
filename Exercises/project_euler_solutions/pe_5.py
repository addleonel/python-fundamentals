"""
problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series,
1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def series(to_number):
    tn = to_number
    s = 0
    for k in range(1, tn + 1):
        s += k**k
    return s

#print(series(1000))
    
"""
problem 30
Surprisingly there are only three numbers
that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that
can be written as the sum of fifth powers of their digits.
"""
def split_number(number):
    n = number
    digits = []
    while n > 0:
        r = n%10
        n = n//10
        digits.append(r)
    digits.sort()
    return digits

def operation(number, power):
    s = 0
    digits = split_number(number)
    for k in digits:
        s += k**power
    if s == number:
        yield number

def find(to_number, power):
    n = 2
    s = 0
    while True:
        for k in operation(n, power):
            print(k)
            s += k
            print("sum: {}".format(s))
        n += 1

find(10000, 5)
        
    




















