"""
    Use 'suoer()' with simple inheritance and
    if you want to use multiple inheritance call from the son class with a
    instance of constructors from Father classes

"""

class Father:
    def __init__(self, cara, ojosazules, nariz, estatura):
        self.cara = cara
        self.ojosazules = ojosazules
        self.nariz = nariz
        self.estatura = estatura

    @staticmethod
    def my_description():  # this a static method, because don't change output of the method
        print("I am the father")

    def iam(self):  # this is a instance method because have 'self'
        print("cara: {} \nojo: {} \nNariz: {} \nEstatura: {}".format(
            self.cara,
            self.ojosazules,
            self.nariz,
            self.estatura
        ))


class Mother:
    def __init__(self, caracter, color_cabello):
        self.caracter = caracter
        self.color_cabello = color_cabello

    @staticmethod
    def my_description():  # this a static method, because don't change output of the method
        print("I am the Mother")

    def iam(self):  # this is a instance method because have 'self'
        print("caracter : {} \ncabello: {}".format(
            self.caracter,
            self.color_cabello
        ))


class Son(Father, Mother):  # preference to Father
    def __init__(self, cara, ojosazules, nariz, estatura, caracter, color_cabello, arte):
        Father.__init__(self, cara, ojosazules, nariz, estatura)  # attribute from Father
        Mother.__init__(self, caracter, color_cabello)
        self.arte = arte

    @staticmethod
    def my_description():
        print(" I am the son")

    def iam(self):  # this is a instance method because have 'self'
        print("cara: {} \nojo: {} \nNariz: {} \nEstatura: {} \ncaracter : {} \ncabello: {} \narte: {}".format(
            self.cara,
            self.ojosazules,
            self.nariz,
            self.estatura,
            self.caracter,
            self.color_cabello,
            self.arte
        ))


class Daughter(Mother, Father):  # preference to Mother if create a 'super'
    def __init__(self, cara, ojosazules, nariz, estatura, caracter, color_cabello, science):
        Mother.__init__(self, caracter, color_cabello)  # this the attribute from Mother
        Father.__init__(self, cara, ojosazules, nariz, estatura)
        self.science = science

    @staticmethod
    def my_description():
        print("I am the Daughter")

    def iam(self):  # this is a instance method because have 'self'
        print("cara: {} \nojo: {} \nNariz: {} \nEstatura: {} \ncaracter : {} \ncabello: {} \nscience: {}".format(
            self.cara,
            self.ojosazules,
            self.nariz,
            self.estatura,
            self.caracter,
            self.color_cabello,
            self.science
        ))


# out of class
father = Father("cara de padre", "ojos de padre", "nariz de padre", "estatura de padre")
father.my_description()
father.iam()

print("-"*40)

mother = Mother("caracter de madre", "brown")
mother.my_description()
mother.iam()

print("-"*40)

son = Son("cara de hijo", "ojo de hijo", "nariz de hijo", "estatura de hijo", "caracter de hijo", "cabello de hijo",
          "Me gusta la Pintura")
son.my_description()
son.iam()

print("-"*40)

daughter = Daughter("cara de hija", "ojo de hija", "nariz de hija", "estatura de hija", "caracter de hija",
                    "cabello de hija",
                    "Me gusta la ciencia")
daughter.my_description()
daughter.iam()
