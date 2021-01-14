# PROBLEM 52

# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def compare_digits(num1, num2):
    digist1 = list(str(num1))
    digist2 = list(str(num2))
    digist1.sort()
    digist2.sort()
    if len(digist1) == len(digist2) and digist1 == digist2:
        return True
    return False


def find_():
    x = 0
    valid = 1
    while True:
        x += 1
        valid = 1
        for i in range(2, 6 + 1):
            if compare_digits(x, x*i):
                valid *= 1
            else:
                valid *= 0
        if valid == 1:
            print(x)


if __name__ == '__main__':
    find_()