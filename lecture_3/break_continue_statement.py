# Now I'm going to use 'break' and 'continue' statement
# Also I'm going to use 'pass' statement 
# import the method 'print' from 'ifStatement'


def break_statement_first():
    for num in range(2, 10):
        for divisor in range(2, num):
            if num % divisor == 0:
                print(num, "is not  prime number")
                break
        else:
            print(num, "is prime number")


def break_statement_second(start, end):
    print("The prime numbers between", start, "and", end, "are: ")
    for i in range(start, end):
        for divisor in range(2, i):
            if i % divisor == 0:
                # print("not prime number")
                pass
                break
        else:
            print(i, end=" ")
    print("\r")


def break_statement_third():
    start = float(input("Input inicial number: "))
    end = float(input("Input end number: "))
    for iterator in range(int(start), int(end)):
        for divisor in range(2, iterator):
            if iterator % divisor == 0:
                pass
                break
        else:
            print(iterator, end=" ")
    print("\r")


def continue_statement_first():
    for num in range(1, 20):
        if num % 2 == 0:
            print(num, "is a even number")
            continue
        print(num)


print("-"*30)
break_statement_first()
print("-"*30)
continue_statement_first()
print("-"*40)
break_statement_second(20, 40)
break_statement_second(10, 50)
print("-"*24)
break_statement_third()
