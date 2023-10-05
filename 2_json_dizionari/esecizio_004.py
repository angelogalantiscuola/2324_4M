import json

# Apro il file JSON e carico il dizionario
with open('es1.json', 'r') as file:
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
