import math

def vn(message):
    while True:
        try:
            text = float(input(message))
            return text
        except ValueError:
            print("just number, try again")


def travel_time():
    time = []
    while True:
        minutes = vn("Duration of the section in minutes:")
        time.append(minutes)
        if minutes == 0:
            break
    stime = math.fsum(time)
    # separate decimal part
    decimal, integer = math.modf(stime)
    hour = integer // 60
    minute_1 = integer % 60
    seconds = decimal * 60
    dsecond, isecond = math.modf(seconds)
    print(hour, "h:", minute_1, "m:", isecond, "s    approx. second")


if __name__ == '__main__':
    travel_time()