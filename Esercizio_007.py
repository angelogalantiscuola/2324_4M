class Auto:
    def __init__(self, marca, modello, targa, km_percorsi):
        self.marca = marca
        self.modello = modello
        self.targa = targa
        self.km_percorsi = km_percorsi

    def effettua_viaggio(self, km):
        self.km_percorsi += km
        
auto1 = Auto("Fiat", "Panda", "AB123CD", 50000)
print(auto1.km_percorsi) 

auto1.effettua_viaggio(100)
print(auto1.km_percorsi)  

auto1.effettua_viaggio(50)
print(auto1.km_percorsi)  