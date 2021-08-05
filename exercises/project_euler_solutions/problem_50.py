
"""
problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from exercises.project_euler_solutions.tools.prime_number import is_prime

def primes_below_to(limit):
    sum_ = 0
    prime_numbers = []
    for k in range(2, limit):
        if is_prime(k):
            sum_ += k
            if sum_ > limit:
                break
            prime_numbers.append(k)

    return prime_numbers

def from_beginning(primes_list):
    collect = {}
    arr = [*primes_list]
    while True:
        sum_arr = sum(arr)
        if is_prime(sum_arr):
            collect[sum_arr] = arr
            break
        arr.pop(0)

    arr = [*primes_list]
    while True:
        sum_arr = sum(arr)
        if is_prime(sum_arr):
            collect[sum_arr] = arr
            break
        arr.pop()
    return collect


if __name__ == '__main__':
    LIMIT = 1000000
    primes = primes_below_to(LIMIT)
    collection_ = from_beginning(primes)
    correct_item = {}
    arr_lengths = []
    for value in collection_.values():
        arr_lengths.append(len(value))

    for values_sum, values in collection_.items():
        if len(values) == max(arr_lengths):
            print(values_sum, values)




