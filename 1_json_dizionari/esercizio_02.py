"""
Questo esercizio richiede di creare un programma Python che esegue le seguenti operazioni:

1. Chiede all'utente di inserire i dati per un numero specifico di automobili. I dati per ogni automobile dovrebbero includere dettagli come marca, modello, anno di produzione, ecc.
2. Aggiunge i dati di ogni automobile a una lista di dizionari, dove ogni dizionario rappresenta un'automobile.
3. Salva la lista di dizionari in un file JSON per la persistenza dei dati.

"""

import json

def main():
    # Numero di auto per cui l'utente inserirà i dati
    num_auto = 2

    # Lista per contenere i dati delle auto
    auto_list = []

    # Creazione del dizionario per ogni auto
    for i in range(num_auto):
        marca = input("Inserire la marca dell'auto: ")
        modello = input("Inserire il modello dell'auto: ")
        anno_produzione = int(input("Inserire l'anno di produzione: "))
        potenza = int(input("Inserire la potenza: "))
        
        # Inserimento dei dati dell'auto nel dizionario
        auto_data = dict(marca=marca, modello=modello, anno=anno_produzione, potenza=potenza)
        
        # Aggiunta del dizionario alla lista
        auto_list.append(auto_data)

    # Salvataggio della lista di dizionari in un file JSON
    with open("auto_data.json", "w") as f:
        f.write(json.dumps(auto_list))
