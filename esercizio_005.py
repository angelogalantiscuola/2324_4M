import json


with open("museo.json", "r") as file_json:
    mydict = json.loads(file_json.read())

# Inizializza il museo come un dizionario vuoto
museo = {"stanze": {}, "opere": {}}

# Funzione per salvare i dati nel file JSON
def salva_museo():
    with open('museo.json', 'w') as file:
        json.dump(museo, file)

def cancella_opera(stanze, opere, opera_id):
    if opera_id in opere:
        for stanze, opere_stanza in stanze.items():
            if opera_id in opere_stanza:
                opere_stanza.remove(opera_id)
        del opere[opera_id]
        print(f"Opera con ID '{opera_id}' cancellata con successo!")
    else:
        print(f"Errore: Opera con ID '{opera_id}' non trovata.")

def cancella_stanza(stanze, opere, opera_id):
    if opera_id in opere:
        for stanze, opere_stanza in stanze.items():
            if opera_id in opere_stanza:
                opere_stanza.remove(opera_id)
        del opere[opera_id]
        print(f"Opera con ID '{opera_id}' cancellata con successo!")
    else:
        print(f"Errore: Opera con ID '{opera_id}' non trovata.")

# Menu per l'applicativo
while True:
    print("\nMenu:")
    print("1. Creare una nuova stanza")
    print("2. Aggiungere un opera ad una stanza")
    print("3. Consultare le opere presenti in una stanza")
    print("4. Consultare le stanze presenti")
    print("5. Cancellare un opera")
    print("6. Cancellare una stanza solo se vuota")
    print("7. Esci")

    scelta = input("Inserisci il numero corrispondente all'operazione desiderata: ")

    if scelta == "1":
        nome_stanza = input("Inserisci il nome della nuova stanza: ")
        museo["stanze"][nome_stanza] = []
        print(f"Stanza '{nome_stanza}' creata con successo!")

    elif scelta == "2":
        nome_stanza = input("In quale stanza vuoi aggiungere l'opera? ")
        if nome_stanza in museo["stanze"]:
            titolo = input("Inserisci il titolo dell'opera: ")
            artista = input("Inserisci il nome dell'artista: ")
            anno = input("Inserisci l'anno di creazione: ")
            nuova_opera = {"titolo": titolo, "artista": artista, "anno": anno}
            opera_id = len(museo["opere"]) + 1
            museo["opere"][opera_id] = nuova_opera
            museo["stanze"][nome_stanza].append(opera_id)
            print(f"Opera '{titolo}' aggiunta alla stanza '{nome_stanza}' con successo!")
        else:
            print(f"Errore: La stanza '{nome_stanza}' non esiste.")

    elif scelta == "3":
        nome_stanza = input("Di quale stanza vuoi vedere le opere? ")
        if nome_stanza in museo["stanze"]:
            opere_stanza = museo["stanze"][nome_stanza]
            for opera_id in opere_stanza:
                opera = museo["opere"][opera_id]
                print(f"ID: {opera_id}, Titolo: {opera['titolo']}, Artista: {opera['artista']}, Anno: {opera['anno']}")
        else:
            print(f"Errore: La stanza '{nome_stanza}' non esiste.")

    elif scelta == "4":
        print("Stanze presenti nel museo:")
        for stanza in museo["stanze"]:
            print(stanza)

    elif scelta == "5":
            opera_id = str(input("Inserisci l'ID dell'opera da cancellare: "))
            cancella_opera(museo["stanze"], museo["opere"], opera_id)

    elif scelta == "6":
        nome_stanza = input("Inserisci il nome della stanza da cancellare: ")
        cancella_stanza(museo["stanze"], nome_stanza)

    elif scelta == "7":
            salva_museo()
            print("Grazie per aver visitato il Museo. Arrivederci!")
            break

    else:
        print("Scelta non valida. Riprova.")
