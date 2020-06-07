"""
problem 6:
The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=55^2 = 3025
Hence the difference between the sum of the squares
of the first ten natural numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.

"""
def difference_of_square(to_number):
    tn = to_number
    sigma = square_of_the_sum(tn)-sum_of_the_squares(tn)
    print('{} - {} = {}'.format(square_of_the_sum(tn),sum_of_the_squares(tn),
                                  sigma))

def sum_of_the_squares(number, sum_square = 0):
    sq = sum_square
    for k in range(1, number+1):
        sq += k**2
    return sq

def square_of_the_sum(number, result_sum = 0):
    rs = result_sum
    for k in range(1, number+1):
        rs += k
    return rs**2

# problem 6:
difference_of_square(100)
