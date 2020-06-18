"""
problem 10:
Not solved

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
def is_prime(num):
    divisors = 0
    for k in range(2, num):
        if num % k == 0:
            divisors += 1
    if divisors > 0:
        return False
    elif divisors == 0:
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

