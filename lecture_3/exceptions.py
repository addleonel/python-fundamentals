# MORE INFORMATION
# https://docs.python.org/3/tutorial/errors.html

# class B(Exception):
#   pass

# class C(B):
#   pass

# class D(C):
#   pass

# for cl in [B, C, D]:
#   try:
#     raise cl
#   except D:
#     print("D")
#   except B:
#     print("B")
#   except C:
#     print("C")

# try:
#   raise NameError
#   raise SyntaxError
# except Exception:
#   print("hello there is a error") 

# for k in [NameError, ValueError, SyntaxError]:
#   try:
#     raise k
#   except NameError:
#     print("There is a NameError")
#   except ValueError:
#     print("There is a ValueError")
#   except SyntaxError:
#     print("There is a SyntaxError")


# try:
#     with open("myfile.txt", "r") as f:
#       lines = f.readlines()
#       for l in lines:
#         print(l.strip('\n'))
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# USING try ... except ... else ... finally

for k in [1.0,"two", 3.0]:
    try:
        i = int(k)
    except ValueError:
        print("Error")
    else:
        print("yep")
    finally:
        print("completed process\n"+"="*30)


# If there is a finally clause present, the finally clause will run as the last task
# before try the instruction complete. The finally clause is executed
# regardless of whether or not the try statement throws an exception. The following
# Points discuss more complex cases when an exception occurs:

# 1- If an exception occurs during the execution of the try clause,
#   the exception can be handled by an except clause.
#   If the except clause does not handle the exception,
#   the exception is rebuilt after the finally clause has been executed.
# 2- An exception could occur during the execution of an except or the clause.
#   Again, the exception is rebuilt after finally the clause has been executed.

# 3- If the try statement reaches a break, continue or return communicated,
#   the finally clause will be executed just before the break, continueo return the declaration execution.

# 4- If a finally clause includes a return declaration, the returned value will be the one of
#   the declaration of the finally clause return, not the value of the declaration of the try clause return.

# 1-
# try:
#   raise NameError("Hi error")
# except SyntaxError:
#   print("error SyntaxError")
# finally:
#   print("FINISHED")
# 3-
# n = 0
# while n < 10:
#   try:
#     print(n)
#     if n == 4:
#       break
#     print("Bye")
#   except Exception:
#     print("Error")
#   finally:
#     print("finished")
#   n += 1
# 4-
# def example():
#   try:
#     return True
#   finally:
#     return False
# print(example()) # return False

# CORRECT USE of try ... except ... else ... finally ...

def divide(x, y):
    try:
        r = x/y
    except ZeroDivisionError:
        print("Not divide by zero")
    except TypeError:
        print("Not input an string")
    else:
        print("the result is: {}".format(round(r, 2)))
    finally:
        print("completed process\n" + "="*30)


divide(2, 3)
divide(2, 0)
divide('2', '3')
divide(10, 2)





