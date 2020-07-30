# I'm going to practice "if" Statement

# first example in a function

def ifStatementFirst():
    num = float(input("select a number: "))
    # print from zero to number selected
    for iterator in range(0, int(num) + 1, 1):
        print(iterator, end=" ")
    print()

    if num > 0:
        if num % 2 == 0:
            print("the number ", str(num), " is even")
            print("Its even divisor are: ")
            # even divisors
            for i in range(2, 100, 2):
                if num % i == 0:
                    if i == num:
                        print(i, end=". ")
                    else:
                        print(i, end=", ")
            print("\nIts odd divisor are: ")
            # odd divisor
            for i in range(1, 100, 2):
                if num % i == 0:
                    print(i, end=", ")

        else:
            print("the number ", str(num), " is odd")
            if num % 2 == 0:
                print("Its even divisor are: ")
                # even divisors
                for i in range(2, 100, 2):
                    if num % i == 0:
                        if i == num:
                            print(i, end=". ")
                        else:
                            print(i, end=", ")
            else:
                print("The number don't have even divisor")

            print("Its odd divisor are: ")
            # odd divisor
            for i in range(1, 100, 2):
                if num % i == 0:
                    print(i, end=", ")
    elif num < 0:
        print("this is english")
        print("The number is negative")
    else:
        print("The number is Zero")


# function for print a line and make line break
def printLine(number_script_put_integer, number_line_break_put_integer):

    # this is for number_script_put_integer
    num = 12

    if number_script_put_integer > 0:
        for i in range(number_script_put_integer):
            print("-", end="")  # <end=""> is for print in the same line
        print()
    elif number_script_put_integer == 0:
        # the 'pass' statement make nothing
        pass
    else:
        print(num / 0)

    # this is for number_line_break_put_integer
    if number_line_break_put_integer > 0:
        for j in range(number_line_break_put_integer):
            print()
    elif number_line_break_put_integer == 0:

        pass
    else:
        print(num / 0)


# EXAMPLES ABOUT the method 'printLine()'
# printLine(12, -2)
printLine(0, 0)
print()
printLine(100, 1)

# PUT THE RESULT OF METHODS
ifStatementFirst()


