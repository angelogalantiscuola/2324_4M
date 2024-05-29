"""
crea un programma che legga la lista contenuta nel file JSON creato nel precedente esercizio e fornisca le seguenti funzionalità:

1. calcolo della rata del bollo per le auto contenute nella lista (formula: 2.58*kW(fino a 100kW) + 3.87(sui kW eccedenti))
2. calcolo dell'età media degli autoveicoli presenti nella lista

"""
import json

# Funzione per calcolare la tassa in base alla potenza in kW
def calcola_bollo(potenza_kw):
    if potenza_kw <= 100:
        tassa = potenza_kw * 2.58
    else:
        tassa = 100 * 2.58 + (potenza_kw - 100) * 3.87 
    return round(tassa, 2)

# Funzione per calcolare l'età dell'auto in base all'anno di produzione
def calcola_eta(anno_produzione):
    anno_corrente = 2023
    return anno_corrente - anno_produzione


def main():
    # Carica i dati delle auto dal file JSON
    with open("auto.json", "r") as file:
        auto = json.load(file)

    # Chiede all'utente l'operazione che desidera eseguire
    scelta = int(input("Cosa vuoi fare?\n 1) Calcola bollo\n 2) Calcola età media delle auto\n"))

    # Calcola il bollo per un modello specifico
    if scelta == 1:
        modello = input("Inserisci il modello: ")
        presente = False
        for car in auto:
            if modello == car["modello"]:
                presente = True 

        if presente:
            for car in auto:
                if car["modello"] == modello:
                    print("La rata del bollo è", calcola_bollo(car["potenza_kw"]))
        else:
            print("Modello non trovato!!!")

    # Calcola l'età media delle auto
    elif scelta == 2:
        eta_totale = 0
        for car in auto:
            eta_totale += calcola_eta(car["anno_produzione"])

        eta_media = eta_totale / len(auto)
        print("L'età media delle auto è", eta_media, "anno/i")

    else:
        print("Opzione non valida")
