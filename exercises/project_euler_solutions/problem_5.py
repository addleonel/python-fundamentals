"""
problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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
        
def find_numbers(from_number, to_number):
    
    max_number = 1
    min_number = 1
    c = 0
    many = 0
    for i in range(from_number, to_number + 1):
        max_number*=i
        if is_prime(i):
           min_number*=i 
    # print(max_number)
    # print(min_number)
    
    for k in range(min_number, max_number):
        for i in range(from_number, to_number + 1):
            if k % i == 0:
                c += 1
        if c == to_number:
            many+=1
            yield k
        c = 0
        if many == 2:
            break
        
   
# problem 5:

for k in find_numbers(1, 20):
    print(k)





