"""
problem 10:
Not solved

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
def prime_number(possible_prime = 2):
    while True:
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False
        if is_prime:
            yield possible_prime
        possible_prime += 1

def sum_prime_number(below_of):
    primes = prime_number()
    prime = next(primes)
    while prime < below_of:
        print(prime)
        yield prime
        prime = next(primes)

# problem 10:
"""
Note:
no pertenece a ninguna variable por lo tanto
los dos print() imprimiran lo mismo
print(next(prime_number())) # 2
print(next(prime_number())) # 2

solo pertenece a la pariable 'p'
p = prime_number()
print(next(p)) # 2
print(next(p)) # 3
print(next(p)) # 5
print()
solo pertenece a la pariable 's'
s = prime_number()
print(next(s)) # 2
print(next(s)) # 3
print(next(s)) # 5
print(next(s)) # 7
print(next(s)) # 11
print(next(s)) # 13
print(next(s)) # 17
print(next(s)) # 19
print(next(s)) # 23
"""
print(sum(sum_prime_number(2000000)))
