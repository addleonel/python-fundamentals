
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



