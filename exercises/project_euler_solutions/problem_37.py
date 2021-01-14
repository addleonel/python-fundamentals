
# PROBLEM 37

# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from exercises.project_euler_solutions.tools.prime_number import is_prime

def is_truncatable(num):
    digits1 = list(str(num))
    digits2 = digits1.copy()
    valid = 1
    num1 = num2 = num
    if is_prime(num):
        for _ in range(0, len(digits1)):
            if is_prime(num1) and is_prime(num2):
                valid *= 1
            else:
                valid *= 0
            if len(digits1) == 1:
                break
            digits1.pop(0)
            digits2.pop(-1)
            num1 = int(''.join(digits1))
            num2 = int(''.join(digits2))
        if valid == 1:
            return True
        return False
    else:
        return False


if __name__ == '__main__':

    k = 8
    sum_ = 0
    count = 0
    while True:
        k += 1
        if is_truncatable(k):
            count += 1
            sum_ += k
            if count == 11:
                print(sum_)
                break
        else:
            continue
