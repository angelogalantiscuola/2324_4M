#Create a Python program that models a 1-1 association between two classes, Person and Passport.
#
#The Person class should have the following attributes:
#
#name: a string that represents the name of the person. age: an integer that represents the age of the person. passport: an instance of the Passport class that represents the person's passport. This should initially be None. The Person class should also have a method issue_passport that takes a passport number and a country of issue as parameters, creates a new Passport object, and assigns it to the passport attribute.
#
#The Passport class should have the following attributes:
#
#passport_number: a string that represents the passport number. country_of_issue: a string that represents the country of issue.
#
#(Optional: person: an instance of the Person class that represents the passport holder. This should initially be None. The Passport class should also have a method set_person that takes a Person object as a parameter and assigns it to the person attribute.)
#
#Demonstrate the 1-1 association by creating a Person object, using the issue_passport method to create a Passport object.
#
#Note: In a 1-1 association, an instance of a class (e.g., Person) is associated with exactly one instance of another class (e.g., Passport), and vice versa.


class Persona:
    def __init__(self, nome, eta):
        self.nome = nome    #Attributi
        self.eta = eta      #Attributi
        self.Passaporto = ""    #Attributi

    def param_Passaporto(self, Passaporto_numero, paese):  #Metodo
        self.Passaporto = Passaporto(Passaporto_numero, paese)      
        self.Passaporto.set_person(self)        

class Passaporto:
    def __init__(self, Passaporto_numero, paese):
        self.Passaporto_numero = Passaporto_numero      #Attributi
        self.paese = paese      #Attributi
        self.persona = ""       #Attributi

    def set_person(self, persona):      #Metodo
        self.persona = persona
        

person = Persona("Franco", 17)      #Creazione oggetto
person.param_Passaporto("QW13245RW", "ITALIA")      #Creazione oggetto
print(person.Passaporto.Passaporto_numero)    #Stampa attributo
print(person.Passaporto.paese)                #Stampa attributo
print(person.Passaporto.persona.nome)         #Stampa attributo
print(person.Passaporto.persona.eta)          #Stampa attributo