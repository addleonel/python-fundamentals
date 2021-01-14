# PROBLEM 36

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindromic(num):
    n1 = list(str(num))
    n2 = n1.copy()
    n2.reverse()
    if n1 == n2:
        return True
    return False

def to_binary(num):
    digits = []
    while num > 0:
        r = num % 2
        digits.append(r)
        num = num // 2
    digits.reverse()
    return int(''.join([str(i) for i in digits]))


if __name__ == '__main__':

    LIMIT = 1000000
    sum_ = 0

    for k in range(1, LIMIT):
        if is_palindromic(k) and is_palindromic(to_binary(k)):
            sum_ += k

    print(sum_)