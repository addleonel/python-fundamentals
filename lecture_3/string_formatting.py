# There are three ways to write a the same message
import math
name = 'Alan Turing'
age = 23
pinum = math.pi
# Old way Python 2.7
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
message1 = 'Hello my name is %s and I am %d years old' % (name, age)
message2 = 'Pi is %.4f' % pinum  # it means four digits after the point

# Python 3
# 'format' method

# Empty brackets {}
message3 = 'Hello my name is {} and I am {} years old'.format(name, age)
# With index into brackets
message4 = 'Hello my name is {0} and I am {1} years old'.format(name, age)
# Keyword arguments are called
message5 = 'Hi! my name is {name} and I am {age} year old'.format(name=name, age=age)
# type specifying:
# s – strings
# d – decimal integers (base-10)
# f – floating point display
# c – character
# b – binary
# o – octal
# x – hexadecimal with lowercase letters after 9
# X – hexadecimal with uppercase letters after 9
# e – exponent notation
# Syntax :
# String {field_name:conversion} Example.format(value)
message6 = 'Today is {1} and the temperature is {0:f} degrees'.format(25.34, 'monday')
message7 = 'The average is {0:.2f}'.format(13.23682)  # it means 2 digits after the point
message8 = 'The {0} of {1} is {1:b}'.format('binary', 324)
message9 = 'The {0} of {1} is {1:e}'.format('octal', 32233)
# Padding Substitutions or Generating Spaces :
# <   :  left-align text in the field
# ^   :  center text in the field
# >   :  right-align text in the field
message10 = 'The great number is --{0:^10}--'.format(234)  # center text
message11 = 'I found the victory with --{0:<9}--'.format(234)  # left-align text
message12 = '{0:*^11b}'.format(345)  # output *101011001*

# Python 3.6 +
# f-string
# we can use the same 'type specifying' as format method
message13 = f'Hello my name is {name} and I am {age} years old'
a = 23
b = 11
# Multiline f-string
message14 = f'{a} + {b} is equal to {a+b} and its double is {2*(a+b)}. \n'\
            f'{a} * {b} is equal to {a*b}. \n'\
            f'{a} / {b} is equal to {a/b}. \n'\
            f'{a} and {b} in binary are {a:b} and {b:b} respectively'

# example using a function
def number_table(from_, to_):
    """
    A function that prints number with exponential
    """
    global ln_  # global variable just to this function
    c = 0
    line = '-'
    n1, n2, n3, n4 = 'n', 'n**2', 'n**3', 'n**4'
    ln_ = 45
    for k in range(from_, to_ + 1):
        msg = f'|{k:6d} |{k ** 2:6d} |{k ** 3:6d} |{k ** 4:6d}|'
        ln_ = len(msg)
        if c == 0:
            print(f'|{n1:>6s} |{n2:>6s} |{n3:>6s} |{n4:>6s}|')
            print(f'{line * ln_}')
        print(msg)
        c += 1
    else:
        print(f'{line * ln_}')


print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)
print(message8)
print(message9)
print(message10)
print(message11)
print(message12)
print(message13)
print(message14)
number_table(1, 9)