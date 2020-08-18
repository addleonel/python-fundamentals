
"""
problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from exercises.project_euler_solutions.tools.prime_number import is_prime

def evaluate_below_(number):
    sum_ = 0
    counter = 0
    primes_with_longest_sum = {}
    for k in range(2, number):
        if is_prime(k):
            # print(k)
            sum_ += k
            counter += 1
            if is_prime(sum_):
                # print(sum_, counter)

                primes_with_longest_sum[counter] = sum_
                # print(primes_with_longest_sum)

    print(primes_with_longest_sum)
    longest_sum_keyword = max(primes_with_longest_sum.keys())

    return primes_with_longest_sum[longest_sum_keyword]


print(evaluate_below_(1000))



