"""

Realizzare un applicativo che permetta, mediante l'uso di dizionari, 
liste e file JSON, la gestione del catalogo di un museo.

In particolare, l'applicativo dovrà permettere di:
4) Consultare le stanze presenti
5) Cercare le informazioni su un opera
6) Cancellare un opera
7) Cancellare una stanza solo se vuota

NB 
- Ad ogni cambiamento, aggiornare il file JSON che garantisce la persistenza. 
- Realizzare un menù numerato con le varie funzionalità elencate in precedenza.

"""

import json

# 1) Creare una nuova stanza
def crea_stanza(museo: dict):
    # input
    nome_stanza = input("Inserisci il nome della stanza: ")
    # elaborazione
    stanza = {
        "nome": nome_stanza,
        "opere": [],
    }
    # controllo se la stanza è già presente
    for stanza in museo["stanze"]:
        if stanza["nome"] == nome_stanza:
            print("La stanza è già presente!")
            return None
    museo["stanze"].append(stanza)
    # output
    print("Stanza creata con successo!")
    return stanza

# 2) Aggiungere un opera ad una stanza(titolo, artista, anno)
def aggiungi_opera(museo: dict):
    # input
    nome_stanza = input("Inserisci il nome della stanza: ")
    titolo_opera = input("Inserisci il titolo dell'opera: ")
    artista_opera = input("Inserisci l'artista dell'opera: ")
    anno_opera = int(input("Inserisci l'anno dell'opera: "))
    # elaborazione
    opera = {
        "titolo": titolo_opera,
        "artista": artista_opera,
        "anno": anno_opera,
    }
    # controllo se la stanza è già presente
    for stanza in museo["stanze"]:
        if stanza["nome"] == nome_stanza:
            # controllo se l'opera è già presente nella stanza
            # TODO meglio controllare se l'opera è univoca in tutto il museo
            for opera in stanza["opere"]:
                if opera["titolo"] == titolo_opera:
                    print("Opera già presente!")
                    return None
            stanza["opere"].append(opera)
            print("Opera aggiunta con successo!")
            return opera
    print("Stanza non presente!")
    return None

# 3) Consultare le opere presenti in una stanza
def cerca_stanza(museo: dict, nome_stanza: str) -> dict:
    # elaborazione
    for stanza in museo["stanze"]:
        if stanza["nome"] == nome_stanza:
            return stanza
    return None

def stampa_opere_stanza(stanza: dict) -> None:
    # output
    if stanza is not None:
        print("Opere presenti nella stanza:")
        for opera in stanza["opere"]:
            print(opera["titolo"])
    else:
        print("Stanza non presente!")

museo = {
    "nome": "Museo di Roma",
    "stanze": [],
}

museo["stanze"].append(
    {"nome": "Rinascimento", "opere": 
    [{"titolo": "La creazione di Adamo", "artista": "Michelangelo", "anno": 1512}]
    }
    )
# crea_stanza(museo)
# aggiungi_opera(museo)

# stampa opere della stanza
nome_stanza = "dfsdfsdfsdfs"
stanza = cerca_stanza(museo, nome_stanza)
stampa_opere_stanza(stanza)

# stampa opere della stanza
nome_stanza = "Rinascimento"
stanza = cerca_stanza(museo, nome_stanza)
stampa_opere_stanza(stanza)
