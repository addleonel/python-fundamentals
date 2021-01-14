# PROBLEM 56

# A googol (10100) is a massive number: one followed by one-hundred zeros;
# 100100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?


def digit_adding(num):
    sum_ = 0
    while num > 0:
        r = num % 10
        sum_ += r
        num = num // 10
    return sum_


def powerful():
    compare_: list = []
    value: int
    max_: int = 0
    for i in range(1, 100):
        for j in range(1, 100):
            value = digit_adding(i**j)
            compare_.append(value)
            if len(compare_) == 2:
                max_ = max(compare_)
                compare_.clear()
                compare_.append(max_)
    return compare_[0]


if __name__ == '__main__':
    print(powerful())