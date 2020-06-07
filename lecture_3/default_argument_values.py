# I'm going to use deafult argument values in function


# introduce_DATA
def enter_NAME():
    name = input("Your name: ")
    return name


def enter_SURNAME():
    surname = input("your surname: ")
    return surname


def enter_AGE():
    age = int(input("your age: "))
    return age


def enter_GENDER():
    gender = input("your gender: ")
    return gender


def enter_ADDRESS():
    address = input("your address: ")
    return address


def enter_TELEPHONENUMBER():
    phone = input("your telephone number: ")
    return


def defaultArgumentValues_FIRST(name=enter_NAME(), surname=enter_SURNAME(), age=enter_AGE(),
                                gender=enter_GENDER(), address=enter_ADDRESS(), phone=enter_TELEPHONENUMBER()):
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


def next_SECOND(valor, lst=None):
    if lst is None:
        lst = []
    lst.append(valor)
    return lst


# print(next_(1))
# print(next_(2))
# print(next_(123))
next_SECOND(12)

# ALL RESULT
# defaultArgumentValues_FIRST()
# tuple = (12, 12, 13, "reminder", "retry", "opportunity")
input_ok("Write a yes or no: ")
