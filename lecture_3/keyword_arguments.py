# I'm going to use the keyword arguments in a function

def temperatures(value_input='input a temperature in celsius:', conti='Do you want to continue?(y/n):'):
    # calculus
    while True:
        celsius = validation_input_number(value_input)
        kelvin = change_to_kelvin(celsius)
        fahrenheit = change_to_fahrenheit(celsius)
        print("CELSIUS:", celsius)
        print("KELVIN:", kelvin)
        print("FAHRENHEIT:", fahrenheit)
        question = validation_input_string(conti)
        if question in ("y", "yes", "ys", "yep"):
            continue
        elif question in ("n", "no", "not", "nop"):
            break


def change_to_kelvin(value):
    return value + 273.15


def change_to_fahrenheit(value):
    return 9 / 5 * value + 32


def validation_input_number(message):
    while True:
        try:
            message = float(input(message))
            return message
        except ValueError:
            print("Type a number")


def validation_input_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("just integer number: ")


def validation_input_string(message):
    while True:
        mess = input(message)
        if mess in ("y", "yes", "ys", "yep", "n", "no", "not", "nop"):
            return mess
        else:
            print("ingresa \'y\' or \'n\'")
            continue


def usingKeywordsArgumentsFirst(simple_argument, *args, **kwargs):
    print("this is a simple argument:", simple_argument)
    print("this is arguments using  *args:")
    for argument in args:
        print(argument)
    print("this is argument using **kwargs")
    for kw in kwargs:
        print(kw, ":", kwargs[kw], end=", ")


# I'm going to use the arbitrary argument list
def usingKeywordsArgumentsSecond(*args):
    print(*args, sep="-")


def usingKeywordsArgumentsThird():
    list_messages = []
    number_input = validation_input_int("number of inputs: ")
    for iterator in range(number_input):
        mess = input("print any message: ")
        list_messages.append(mess)
    # just put '*' before the list and it will be a string
    print(*list_messages, sep="\n")


def usingKeywordsArgumentsFourth():
    # create a dictionary
    dictionary_one = {
        "name": "Galileo",
        "surname": "Galilei",
        "age": 76,
        "country": "Italy",
    }
    for kw in dictionary_one:
        print(kw, ":", dictionary_one[kw])


# RESULT
temperatures()
usingKeywordsArgumentsFirst("simple argument",
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
usingKeywordsArgumentsSecond(1, 2, 3, 4, 5, 6)
usingKeywordsArgumentsThird()
usingKeywordsArgumentsFourth()
