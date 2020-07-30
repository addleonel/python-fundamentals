# I'm going to use default argument values in function


# introduce data
def enter_name():
    name = input("Your name: ")
    return name


def enter_surname():
    surname = input("your surname: ")
    return surname


def enter_age():
    age = int(input("your age: "))
    return age


def enter_gender():
    gender = input("your gender: ")
    return gender


def enter_address():
    address = input("your address: ")
    return address


def enter_telephone_number():
    phone = input("your telephone number: ")
    return phone


def defaultArgumentValues(name=None, surname=None, age=None, gender=None, address=None, phone=None):
    print("THIS IS ALL YOUR INFORMATION: ")
    print("name:", name, "\nsurname:", surname, "\nage:", age, "\ngender:", gender, "\naddress:", address,
          "\ntelephone number:", phone)


def input_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('yes', 'ys', 'y'):
            print("confirmed")
        if ok in ('nop', 'no', 'n', 'nope'):
            print("no confirmed")
        retries = retries - 1
        if retries < 0:
            print("process finished")
            break
        print(reminder)


def next_(valor, lst=[]):
    lst.append(valor)
    return lst


def next_second(valor, lst=None):
    if lst is None:
        lst = []
    lst.append(valor)
    return lst


# ALL RESULT

print(next_(1))
print(next_(2))
print(next_(123))
next_second(12)
input("Enter to continue...")
defaultArgumentValues()
input("Enter to continue...")
defaultArgumentValues(enter_name(), enter_surname(), enter_age(), enter_gender(),
                      enter_address(), enter_telephone_number())
input("Enter to continue...")
input_ok("Write a yes or no: ")
input("Enter to continue...")