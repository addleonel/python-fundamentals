# EXCEPTIONS
# More info: https://docs.python.org/3/tutorial/errors.html
# Advice: Only concentrate on the exceptions

def sequence_of_the_exceptions():
    """
    If an exception occurs during the execution of the try clause,
    the exception can be handled by an except clause.
    If the except clause does not handle the exception,
    the exception is rebuilt after the finally clause has been executed.
    """
    try:
        raise NameError("Hi error")
    except SyntaxError:
        print("Error SyntaxError")
    finally:
        print("Finished")


def behavior_with_break_continue_statements():
    """
    If the try statement reaches a break, continue or return communicated,
    the finally clause will be executed just before the break,
    continue return the declaration execution.
    """
    n = 0
    while n < 10:
        try:
            print(n)
            if n == 4:
                break
            print("Bye")
        except Exception:
            print("Error")
        finally:
            print("finished")
        n += 1


def behavior_of_return_in_try_finally():
    """
    If a finally clause includes a return declaration,
    the returned value will be the one of
    the declaration of the finally clause return,
    not the value of the declaration of the try clause return.
    """
    try:
        return True
    finally:
        return False

# CORRECT USE OF try, except, else, finally keywords
# syntax: try ... except ... else ... finally

# example 1
def through_list(list_):
    """
    Evaluate if is valid convert each values of the list
    to integer
    """
    for k in list_:
        try:
            i = int(k)
        except ValueError:
            print("Error")
        else:
            print("Yep")
        finally:
            print("Completed process\n"+"="*30)

# example 2
def divide(x, y):
    """
    Evaluate if is valid divide 'x' value by 'y' value
    """
    try:
        r = x/y
    except ZeroDivisionError:
        print('Not divide by zero')
    except TypeError:
        print('Not input an string')
    else:
        print(f'The result is: {round(r, 2)}')
    finally:
        print('Completed process\n' + '='*30)

# USING raise

# example 1
def concat_by(string_):
    """
    Concat string_ value. If this value is not a string
    print and message error
    """
    if not isinstance(string_, str):
        raise ValueError('Only strings')
    return 'Your message is: ' + string_


if __name__ == '__main__':
    # sequence_of_the_exceptions()
    # behavior_with_break_continue_statements()
    through_list([1.0, 'two', 3])  # Yep Error Yep
    divide(2, 3)  # the result is: 0.67
    divide(2, 0)  # Not divide by zero
    divide('2', '3')  # Not input an string
    divide(10, 2)  # the result is: 5.0
    print(concat_by('Through the eyes'))  # Your message is: Though the eyes
    # print(concat_by(32))  # Only strings
    print(behavior_of_return_in_try_finally())  # return False


