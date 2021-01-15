# PROBLEM 63

# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

def power_digit_counts():
    num = 0
    count = 0
    power_ = 1
    while True:
        num += 1
        result = num**power_
        if len(str(result)) > power_:
            power_ += 1
            num = 1
            print(power_)
            continue
        if len(str(result)) == power_:
            count += 1
            print(result, count)


if __name__ == '__main__':
    power_digit_counts()