# I'm going to use the filter method

listNumber = [12, 34, 45, 6, 6, 8, 12, 79]

def number_pair(num):
    if num % 2 == 0:
        return True


print(list(filter(number_pair, listNumber)))

# using the lambda expression
listNumberTwo = [12, 34, 45, 6, 6, 8, 12, 79]
print(list(filter(lambda x: x % 2 == 0, listNumberTwo)))


# with a class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return "{} es {} y tiene un salary de {}".format(self.name, self.position, self.salary)


# out of the class
list_Employees = [
    Employee("Tom", "Director", 50000),
    Employee("John", "vice principal", 30000),
    Employee("Tommy", "Manager", 20000),
    Employee("Homer", "Admin", 18000),
    Employee("Daniel", "Companion", 15000),
    Employee("Mark", "Bellboy", 10000),
]

up_salaries = filter(lambda e: e.salary > 17000, list_Employees)

for k in up_salaries:
    print(k)
