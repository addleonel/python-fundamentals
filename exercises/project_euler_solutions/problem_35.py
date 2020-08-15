"""
problem 35

"""

# is prime
# 2, 3, 5, 7, 11, 13, 17
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


def is_circular_prime(num):
    l_ = [int(k) for k in list(str(num))]
    is_circular_prime_ = True
    for _ in range(len(l_)):
        f_elem = l_.pop(0)
        l_.append(f_elem)
        n = int("".join([str(k) for k in l_]))
        # print(n)
        is_circular_prime_ *= is_prime(n)
        # print(l_)
    return bool(is_circular_prime_)


def below_to(num):
    for k in range(1, num):
        if is_circular_prime(k):
            yield k


c = 0
for k in below_to(1000000):
    print(k)
    c += 1
else:
    print("answer =", c)

