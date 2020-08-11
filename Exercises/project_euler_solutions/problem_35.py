"""
problem 35

"""

# is prime
# 2, 3, 5, 7, 11, 13, 17
def is_prime(number):
    if number == 2:
        return True
    if number == 3:
        return True
    for k in range(4, number):
        if number % k == 0:
            return False
    return True


def is_circular_prime(num):
    all_primes = []
    l_ = [int(k) for k in list(str(num))]
    for _ in range(len(l_)):
        all_primes.append(l_)
        print(l_)
        print(all_primes)
        f_elem = l_.pop(0)
        l_.append(f_elem)
        all_primes.append(l_)
        print(l_)
        print(all_primes)


def below_to(num):
    for k in range(1, num):
        if is_circular_prime(k):
            yield k


is_circular_prime(45)
