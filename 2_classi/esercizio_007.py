#Classe
class  Auto:
    def __init__(self, marca, modello, targa, km_percorsi):
        self.marca=marca
        self.modello=modello
        self.targa=targa
        self.km_percorsi=km_percorsi
    def effetua_viaggio(self,km):
        self.km_percorsi=(km+self.km_percorsi)
        
auto1=Auto("Audi","R6","FF345MR",1244)
#dati necessari per il calcolo
auto1.effetua_viaggio(10000)
print(auto1.km_percorsi)
