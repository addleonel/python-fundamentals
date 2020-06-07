"""
problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series,
1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def series(to_number):
    tn = to_number
    s = 0
    for k in range(1, tn + 1):
        s += k**k
    return s

print(series(1000))
