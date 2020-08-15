"""
problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
def prime_numbers(to_number):
    tn = to_number
    for possible_prime in range(2, tn+1):
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False

        if is_prime:
            yield possible_prime

def the_prime_number_in(position, count = 1):
    c = count
    for i in prime_numbers(900000000):
        print('in position = {} -> value of prime number = {}'.format(c, i))
        if c == position:
            print('Finished process')
            break
        c += 1

# problem 7:
the_prime_number_in(10001)
