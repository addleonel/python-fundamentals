# PROBLEM 41
# We shall say that an n-digit number is pandigital if it makes
# use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from exercises.project_euler_solutions.tools.prime_number import is_prime

def find_digits(number):
    r = 0
    digits = []
    while number > 0:
        r = number % 10
        digits.append(r)
        number = number//10
    return digits

def repeat(num):
    for d in num:
        if num.count(d) > 1:
            return True
    return False

def pandigital_prime():
    k = 2
    valid = 1
    while True:
        k += 1
        valid = 1
        if not repeat(find_digits(k)):
            for i in range(1, len(find_digits(k)) + 1):
                if str(i) in str(k):
                    valid *= 1
                else:
                    valid *=0

            if valid == 1 and is_prime(k):
                print('YEP', k)


if __name__ == '__main__':
    pandigital_prime()