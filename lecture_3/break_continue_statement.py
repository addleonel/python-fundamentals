# Now I'm going to use 'break' and 'continue' statement
# Also I'm going to use 'pass' statement 
# import the method 'printLine' from 'ifStatement'

from fundamentals.Class_3_MoreControlFlowTools.ifStatement import printLine


def breakStatement_FIRST():
    for num in range(2, 10):
        for divisor in range(2, num):
            if num % divisor == 0:
                print(num, "is not  prime number")
                break
        else:
            print(num, "is prime number")


def breakStatement_SECOND(i_INICIAL, i_FINAL):
    print("The prime numbers between", i_INICIAL, "and", i_FINAL, "are: ")
    for i in range(i_INICIAL, i_FINAL):
        for divisor in range(2, i):
            if i % divisor == 0:
                # print("not prime number")
                pass
                break
        else:
            print(i, end=" ")
    print()


def breakStatement_THIRD():
    INITIAL = float(input("Input inicial number: "))
    FINAL = float(input("Input final number: "))
    for iterator in range(int(INITIAL), int(FINAL)):
        for divisor in range(2, iterator):
            if iterator % divisor == 0:
                pass
                break
        else:
            print(iterator, end=" ")
    print()


def continueStatement_FIRST():
    for num in range(1, 20):
        if num % 2 == 0:
            print(num, "is a even number")
            continue
        print(num)


printLine(30, 0)
breakStatement_FIRST()
printLine(30, 0)
continueStatement_FIRST()
printLine(40, 0)
breakStatement_SECOND(20, 40)
breakStatement_SECOND(10, 50)
printLine(24, 0)
breakStatement_THIRD()
