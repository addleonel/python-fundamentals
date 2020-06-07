# I'm goint to practice "if" Statement

# first example in a function

def ifStatement_FIRST():
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


def prueba(num):
    for i in range(1, 100):
        if num % i == 0:
            print(i, end=" ")


# function for print a line and make line break
def printLine(numberScript_PUT_INTEGER, numberLineBreak__PUT_INTEGER):

    # this is for numberScript_PUT_INTEGER
    num = 12

    if numberScript_PUT_INTEGER > 0:
        for i in range(numberScript_PUT_INTEGER):
            print("-", end="")  # <end=""> is for print in the same line
        print()
    elif numberScript_PUT_INTEGER == 0:
        # the 'pass' statement make nothing
        # En cambio pass simplemente no hace nada y pasa a la siguiente instrucción
        pass
    else:
        print(num / 0)

    # this is for numberLineBreak__PUT_INTEGER
    if numberLineBreak__PUT_INTEGER > 0:
        for j in range(numberLineBreak__PUT_INTEGER):
            print()
    elif numberLineBreak__PUT_INTEGER == 0:

        pass
    else:
        print(num / 0)


# EXAMPLES ABOUT the method 'printLine()'
# printLine(12,-2)
# print("hello")
# printLine(0,0)
# printLine(100,1)
# print("other text")

# PUT THE RESULT OF METHODS
# ifStatement_FIRST()


