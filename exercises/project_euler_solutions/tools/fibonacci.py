
# More info about this:
# https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series

# One way "from the bottom up"
def fib_ls(n):
    """
    This return a list with n items.
    For example if n=5, this returns [0, 1, 1, 2, 3]
    and its length of the list is 5
    """
    fibo_ls = [0, 1]
    for _ in range(2, n):
        fibo_ls.append(fibo_ls[-1] + fibo_ls[-2])
    return fibo_ls

# Just count up a naïve iterative solution
def fib(n):
    """
    This returns a fibonacci number
    For example: if n=3 this returns 2, because
    from 0, 1, 1, 2 the third number of the sequence is 2
    a, b = 0, 1 means a=0 and b=1
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':

    print(f'length={len(fib_ls(10))}, {fib_ls(10)}')
    print(fib(3))  # 2, the third number of the sequence
    for k in range(3):
        print(fib(k))  # output: 0 1 1
