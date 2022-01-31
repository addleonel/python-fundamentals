# I'm going to solve a series of exercises from 'codejam'
# I hope I can solve at least one


def exercise1():
    n = input("type \'N\' value: ")
    b = ""
    for i in range(len(n)):
        if n[i] == '4':
            b += '1'
        else:
            b += '0'
    print(b)
    return "{} {}".format(int(b), int(n)-int(b))


def run():
    cases = int(input("cases number: "))
    for k in range(cases):
        print("case #{}: {}".format(k+1, exercise1()))


if __name__ == '__main__':
    run()
