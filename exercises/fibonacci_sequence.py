# FIBONACCI SEQUENCE
# ==================
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Info about its calculation:
# https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series

# Calculate them using recursive function
# This is a primitive recursive solution
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))  # output: 8
# this means, obtaining the 6+1th of the sequence

# print 6 values of the sequence: 0, 1, 1, 2, 3, 5
for k in range(6):
    print(f'For k={k}, fib_number={fibonacci(k)}')


