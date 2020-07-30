
# when to use __name__ == '__main__'?
# when the Python file (file.py) is compiled the Python interpreter before looping through each line of code
# assign a value to a special variable called __name__
# the value you assign will depend on the behavior of the Python file (Python module)
# the behavior depends on importing the Python file
# when the Python file is not imported, the variable __name__ is assigned as '__main__'
# when the Python file is imported as a module to another module, the Python interpreter assigns the variable __name__
# like the name of the example module: if the module is called file.py then __name__ is equal to 'file'.

def generate_fibonacci():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a = a + b
        b = a + b
        yield a
        yield b


if __name__ == '__main__':
    times = int(input("how many numbers of fibonacci do you want?: "))
    c = 1
    for k in generate_fibonacci():
        print(c, k, sep="->")
        if c == times:
            break
        c = c + 1