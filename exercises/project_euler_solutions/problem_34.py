
"""
problem 34:
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal
to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

def split_number(number):
    n = number
    digits = []
    while n >0:
        r = n%10
        n = n//10
        digits.append(r)
    digits.sort()
    return digits

def factorial_digits():
    c = 3
    st = 0
    lt = []
    while True:
        s = 0
        digits_of_number = split_number(c)
        for k in digits_of_number:
            f = math.factorial(k)
            s += f
        if s == c:
            print(c)
            st += c
            print("sum: {}".format(st))
            lt.append(c) 
        c +=1
    return lt
            
        
    
#print(split_number(123))
#print(math.factorial(1))
print(factorial_digits())




