"""

Leggere il file es1.json contenente un dizionario e stampare a video le chiavi, i valori e la coppia chiavi-valori rispettivamente con i metodi keys(), values() e items().
N.B
1) Il programma dovrebbe funzionare a prescindere dal numero di coppie chiave-valore contenute nel dizionario. 
2) Il formato dell'output dovrebbe essere simile allo screenshot allegato

"""

import json

# Apro il file JSON e carico il dizionario
with open('es004.json', 'r') as file:
    data = json.load(file)

# Stampo le chiavi
print("Chiavi:")
for key in data.keys():
    print(key)

# Stampo i valori
print("\nValori:")
for value in data.values():
    print(value)

# Stampo le coppie chiave-valore
print("\nChiavi-Valori:")
for key, value in data.items():
    print(f"{key}: {value}")
