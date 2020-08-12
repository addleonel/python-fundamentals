"""
problem 10:
Not solved

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
def is_prime(number):
    if number == 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    elif number < 9:
        return True
    else:
        i = 5
        while i*i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i = i + 6
        return True
        
def primes_below_to(num):
        
    for k in range(2, num):
        if is_prime(k):
            yield k


s = 0
for k in primes_below_to(2000000):
    print(k)
    s += k
    
print("-"*30)
print(s)

