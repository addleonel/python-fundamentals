# using functions
def sum_with_input():
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    sum_ = num1 + num2
    return sum_


def print_the_sum(number):
    if number % 2 == 0:
        print("result : ", number)
        print("it's pair")
    else:
        print("result : ", number)
        print("it's odd")


if __name__ == "__main__":
    number_ = sum_with_input()
    print_the_sum(number_)
    print(type(sum_with_input()))

