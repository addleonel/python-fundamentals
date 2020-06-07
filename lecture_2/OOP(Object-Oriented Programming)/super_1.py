# I'm going to use the super() 
class Editorial:
    def __init__(self, name_e, address, phone, email):
        self.name_e = name_e
        self.address = address
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return "EDITORIAL\nName: {}\nAddress: {}\nPhone: {}\nEmail: {}".format(
                self.name_e, self.address, self.phone, self.email
               )

class Author:
    
    def __init__(self, name_a, surname, age, carrer, university):
        self.name_a = name_a
        self.surname = surname
        self.age = age
        self.carrer = carrer
        self.university = university
    
    def __str__(self):
        return "AUTHOR\nname:{}\nsurname:{}\nage:{}\ncarrer:{}\nuniversity:{}".format(
                self.name_a,
                self.surname,
                self.age, 
                self.carrer,
                self.university,
                )


class Libro(Editorial, Author):
    
    def __init__(self, name_l, description, ISBN, amount, name_e, address, phone, email, 
                 name_a, surname, age, carrer, university ):
        self.name_l = name_l
        self.description = description
        self.ISBN = ISBN
        self.amount = amount
        # herencia multiple (otra forma de uso de super)
        Editorial.__init__(self, name_e, address, phone, email)
        Author.__init__(self, name_a, surname, age, carrer, university)
    
    def __str__(self):
        return "Libro bla bla bla"
    
    def info_book(self):
        print(Editorial.__str__(self))
        print(Author.__str__(self))
        print(Libro.__str__(self))
        


libro_1 = Libro("Matematica", "Prohibida reproduccion parcial", 
                "978-612-45216-2-1", 1000, "GEMAR", "AV. Rio Vilcanota 168. Ate. Lima 03",
                "4466176", "rep_gemar09@hotmail.com", "J. Armando", "Venero", 65, 
                "Matematico", "P.U.C.P")
libro_2 = Libro("Matematica", "Prohibida reproduccion parcial", 
                "978-612-45216-2-1", 1000, "GEMAR", "AV. Rio Vilcanota 168. Ate. Lima 03",
                "4466176", "rep_gemar09@hotmail.com", "J. Armando", "Venero", 65, 
                "Matematico", "P.U.C.P")

libro_1.info_book()
print("-"*40)
libro_1.info_book()
print("-"*50)
print(libro_2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    