"""

problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

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
            
# print(is_prime(42))
    
def generate_prime_factors(number):
    
    for k in range(2, number):
        if number % k == 0 and is_prime(k):
            yield k
            

# print the prime factors                
for k in generate_prime_factors(600851475143):
    print(k)






