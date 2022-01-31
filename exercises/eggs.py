# I'm going to solve a exercise called 'huevos a la copa'

import math


def vn(message):
    while True:
        try:
            text = float(input(message))
            return text
        except ValueError:
            print("just number, try again")


def string_validation(message):
    while True:
        text = input(message)
        if text in ("s", "y", "n", "yes", "yeah", "no", "yep", "nop", "not", "si"):
            return text
        else:
            print("type \'y\' or \'n\', please try again")
            continue


def solve_exercise():
    T_0 = vn("type the original temperature: ")
    M = 47
    c = 3.7
    p = 1.038
    K = 0.0054
    PI = math.pi
    E = math.e
    T_w = 100
    T_y = 70
    ln = math.log(((T_0 - T_w) / (T_y - T_w)) * 0.76, E)
    t = ((math.pow(M, 2 / 3) * c * math.pow(p, 1 / 2)) / (K * math.pow(PI, 2) * math.pow(4 * PI / 3, 2 / 3))) * (ln)
    # so convert from second to minute and hours
    minute = t / 60
    hour = minute / 60
    print("""
    
        we know the maxim temperature is 70 °C for the yem 
        and we need the following time:
    """)
    print(t, "in seconds")
    print(minute, "in minutes")
    print(hour, "in hour")


def run():
    # run the program
    solve_exercise()
    # ask if they want to use again
    while True:
        question = string_validation("Do you want to use the program again?(s/n): ")
        if question in ("y", "yes", "yep", "yeah", "s", "si"):
            print("HELLO AGAIN")
            solve_exercise()
        elif question in ("n", "no", "not", "nop"):
            print("GOOD BYE, HAVE A NICE DAY")
            break


if __name__ == '__main__':
    run()
