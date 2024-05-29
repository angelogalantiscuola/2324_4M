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