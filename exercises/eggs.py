# I'm going to solve a exercise called 'huevos a la copa'
# from fundamentals.Class_3_MoreControlFlowTools.lambdaFunction import validation_NUMBER as vn
import math


def vn(message):
    while True:
        try:
            text = float(input(message))
            return text
        except ValueError:
            print("just number, try again")


def stringvalidation(message):
    while True:
        text = input(message)
        if text in ("s", "y", "n", "yes", "yeah", "no", "yep", "nop", "not", "si"):
            return text
        else:
            print("type \'y\' or \'n\', please try again")
            continue


def solvetheexercise():
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


def general():
    # run the program
    solvetheexercise()
    # ask if they want to use again
    while True:
        question = stringvalidation("Do you want to use the program again?(s/n): ")
        if question in ("y", "yes", "yep", "yeah", "s", "si"):
            print("HELLO AGAIN")
            solvetheexercise()
        elif question in ("n", "no", "not", "nop"):
            print("GOOD BYE, HAVE A NICE DAY")
            break


# travel time
def traveltime():
    time = []
    while True:
        minutes = vn("Duracion del tramo en minutos:")
        time.append(minutes)
        if minutes == 0:
            break
    stime = math.fsum(time)
    # separa la parte decimal
    decimal, integer = math.modf(stime)
    hour = integer // 60
    minute_1 = integer % 60
    seconds = decimal * 60
    dsecond, isecond = math.modf(seconds)
    print(hour, "h:", minute_1, "m:", isecond, "s    aprox second")

# calculate the pi value
def pivalue():
    cantidad = int(input("type the number of value: "))
    sum = 0
    for k in range(1,cantidad+1):
        r = math.pow(-1, k+1)/(2*k-1)
        sum = sum + r
    print(4*sum)


# calculate the 'e' value
def evalue():
    e = 0
    m = int(input("type the number of values: "))
    for k in range(m):
        e = e + (1/math.factorial(k))
    print(e)

# general()
# traveltime()
pivalue()
evalue()