# I'm going to use the filter method

# using a method
listNumber = [12, 34, 45, 6, 6, 8, 12, 79]


def number_pair(num):
    if num % 2 == 0:
        return True


print(list(filter(number_pair, listNumber)))

# using the lambda expresion
listNumberTwo = [12, 34, 45, 6, 6, 8, 12, 79]
print(list(filter(lambda x: x % 2 == 0, listNumberTwo)))


# with a class

class Empleado:
    def __init__(self, name, cargo, salario):
        self.name = name
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} es {} y tiene un salario de {}".format(self.name, self.cargo, self.salario)


# out of the class
list_empleados = [
    Empleado("Tom", "Director", 50000),
    Empleado("Jhon", "subdirector", 30000),
    Empleado("Tommy", "gerente", 20000),
    Empleado("Homero", "admin", 18000),
    Empleado("Daniel", "acompañante", 15000),
    Empleado("Mark", "botones", 10000),
]


'''
def l(e):
    if e.salario > 19000:
        return True

up_salaries = filter(l, list_empleados)
'''
up_salaries = filter(lambda e: e.salario > 17000, list_empleados)


for k in up_salaries:
    print(k)
