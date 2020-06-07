# I'm going to use the keyword arguments in a function

def temperatures(value_INPUT='input a temperature in celsius:',
                 conti='Do you want to continue?(y/n):'):
    # calculus
    while True:
        celsius = validation_INPUT_NUMBER(value_INPUT)
        kelvin = changeto_KEVIN(celsius)
        fahrenheit = changeto_FAHRENHEIT(celsius)
        print("CELSIUS:", celsius)
        print("KELVIN:", kelvin)
        print("FAHRENHEIT:", fahrenheit)
        question = validation_INPUT_STRING(conti)
        if question in ("y", "yes", "ys", "yep"):
            continue
        elif question in ("n", "no", "not", "nop"):
            break


def changeto_KEVIN(value):
    return value + 273.15


def changeto_FAHRENHEIT(value):
    return 9 / 5 * value + 32


def validation_INPUT_NUMBER(message):
    while True:
        try:
            message = float(input(message))
            return message
        except ValueError:
            print("ingresa un numero")


def validation_INPUT_INT(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("just integer number: ")


def validation_INPUT_STRING(message):
    while True:
        mess = input(message)
        if mess in ("y", "yes", "ys", "yep", "n", "no", "not", "nop"):
            return mess
        else:
            print("ingresa \'y\' or \'n\'")
            continue


# ------------------------------------------------------------
def usingkeywordsarguments_FIRST(simple_argument, *args, **kwargs):
    print("this is a simple argument:", simple_argument)
    print("this is arguments using  *args:")
    for argument in args:
        print(argument)
    print("this is argument using **kwargs")
    for kw in kwargs:
        print(kw, ":", kwargs[kw], end=", ")


# -------------------------------------------------------------
# I'm going to use the arbitraty argument list
def usingkeywordsarguments_SECOND(*args):
    print(*args, sep="-")


def usingkeywordsarguments_THIRD():
    list_MESSAGES = []
    number_INPUT = validation_INPUT_INT("number of inputs: ")
    for iterator in range(number_INPUT):
        mess = input("print any message: ")
        list_MESSAGES.append(mess)
    # just put '*' before the list and it will be a string
    print(*list_MESSAGES, sep="\n")


def usingkeywordsarguments_FOURTH():
    # create a dictionary
    dictionary_ONE = {
        "name": "Galileo",
        "surname": "Galilei",
        "age": 76,
        "country": "Italy",
    }
    for kw in dictionary_ONE:
        print(kw, ":", dictionary_ONE[kw])

# RESULT
temperatures()
usingkeywordsarguments_FIRST("simple argument",
                             "argument one",
                             "argument two ",
                             "argument three",
                             "argument four",
                             kw_1="value_1",
                             kw_2="value_2",
                             kw_3="value_3",
                             kw_4="value_4",
                             kw_5="value_5",
                             kw_6="value_6",
                             )
usingkeywordsarguments_SECOND(1, 2, 3, 4, 5, 6)
usingkeywordsarguments_THIRD()
usingkeywordsarguments_FOURTH()
