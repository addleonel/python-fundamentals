# -*- coding: utf-8 -*-
# using polymorphism 
# WITH INHERITANCE 
class Country:
    
    # constructor
    def __init__(self, name, language, continent, population):
        self.name = name
        self.continent = continent
        self.population = population
        self.language = language
    
    # methods
    def hope_life(self):
        pass
    
    def product_nacional_bruto(self):
        pass
    
    def indice_desarr_human(self):
        pass
    
    def feature(self):
        pass

    def __str__(self):
        return 'Name: {}\nLanguage: {}\nContinent: {}\nPopulation: {}'.format(
                self.name, self.language, self.continent, self.population
                )
    
class DevelopedCountry(Country):

    def hope_life(self):
        print("""
        Elevada esperanza de vida.
        """)
    
    def product_nacional_bruto(self):
        print("""
        Igual o superior a USD 12 055.
        """)
    
    def indice_desarr_human(self):
        print("""
        Igual o superior a 0,80.
        """)
    
    def feature(self):
        print("""
        - Sector industrial desarrollado.
        - Alto niveles de calidad de vida e ingreso per cápita.
        - Alto índice de desarrollo humano.
        - Fuerte sistema de saludo y una baja tasa de mortalidad infantil.
        - Población cuenta con acceso a la educación y bajo grado de analfabetismo en adultos.
        - Estabilidad política y la desigualdad social es menor que en los países subdesarrollados.
        """)


class UnderdevelopedCountry(Country):

    def hope_life(self):
        print("""
        Esperanza de vida menor a la de los países desarrollados.
        """)
    
    def product_nacional_bruto(self):
        print("""
        Igual o inferior a USD 12 055.
        """)
    
    def indice_desarr_human(self):
        print("""
        Igual o inferior a 0,79
              """)
    
    def feature(self):
        print("""
        - Dependencia del sector agrícola y poco del sector desarrollo industrial.
        - Bajo nivel de calidad de vida e ingreso per cápita.
        - Bajo índice de desarrollo humano.
        - Problemas en salud y mortalidad infantil.
        - Problemas de acceso a la educación y alto grado de analfabetismo en adultos.
        - Puede tener inestabilidad política y desigualdad social.
        """)

    
# create objects   
country1 = DevelopedCountry('United State', 'English', 'America', '327.2 millones (2018)')
country2 = UnderdevelopedCountry('Chad', 'Chad', 'Africa Central', '14.9 millones (2017)')
# country3 = DevelopedCountry()
# country4 = DevelopedCountry()
# country5 = DevelopedCountry()

# create a list for print each objects
list_country = [country1, country2]
for country in list_country:
    print(country)
    print('='*40)
    print('There are {} countries'.format(len(list_country)))

# using a function for print
def description(to_country):
    tc = to_country
    print(tc)
    print('Description:')
    print('      > Esperanza de vida:')
    tc.hope_life()
    print('      > Producto Nacional Bruto:')
    tc.product_nacional_bruto()
    print('      > Indice de Desarrollo Humano:')
    tc.indice_desarr_human()
    print('      > Caracteristicas:')
    tc.feature()

# run description of countries
# description(country1)
# description(country2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    