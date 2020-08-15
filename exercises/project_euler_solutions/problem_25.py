"""
problem 25:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence
 to contain 1000 digits?

"""
def fibonacci_generate():
    a , b = 1, 1
    while True:
        yield a, b
        a = a+b
        b = a+b


def fibo_next():
    for i in fibonacci_generate():
        for j in i:
            yield j

def fibo_generate_to():
    # tn = to_number
    c = 0
    for k in fibo_next():
        c += 1
        yield c, k
        #if c == tn:
         #   break


def digit_number(n):
    digits = []
    while n>0:
        r = n%10
        n = n//10
        digits.append(r)
    return len(digits)


def only_with_digit(n_digits, amount):
    count = 0
    for k in fibo_generate_to():
        if digit_number(k[1]) == n_digits:
            count += 1
            print(k)
            if count == amount:
                break

# problem 25
only_with_digit(1000, 2)
