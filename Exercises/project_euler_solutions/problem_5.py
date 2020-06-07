"""
problem 5
not finished
"""
def smallest_number(to_number):
    tn = to_number
    max= 1
    for k in range(2, tn +1):
        max *= k

    print(max)
    min = max
    for t in range(max, 20, -1):
        if divisible_by(t):
            min = t
            print(min)

def divisible_by(n):
    for k in range(1, 20 +1):
        if n%k !=0:
            return False
    return True
# problem 5:
# don't finished
smallest_number(20)
