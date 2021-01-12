# PROBLEM 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_sequence(n):
    n: int = n
    count: int = 1
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = int(n/2)
            count += 1
        else:
            n = 3*n + 1
            count += 1
    return count


if __name__ == '__main__':
    max_ = 0
    d = {}
    for k in range(1, 1000000):
        d[collatz_sequence(k)] = k
        if len(d) == 2:
            max_ = max(list(d.keys()))
            key_num = max_
            value_ = d.get(key_num)
            d.clear()
            d[key_num] = value_
    print(d)