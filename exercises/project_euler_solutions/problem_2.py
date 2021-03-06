"""
Problem 2:

Each new term in the Fibonacci sequence is generated by adding
the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum of the even-valued terms.

"""
# solving problem 2
def fibonacci():
    a, b = 1, 2
    for k in range(20):
        yield a , b
        a = a + b
        b = a + b

def function_next():
    for i in fibonacci():
        for j in i:
            yield j

def result_sum_fibonacci(arg):
    sum = 0
    print("Even fibonacci numbers:")
    for i in function_next():
        if i%2 == 0 and i<arg:
            print(i)
            sum += i
    print("The sum: {}".format(sum))
result_sum_fibonacci(4000000)
