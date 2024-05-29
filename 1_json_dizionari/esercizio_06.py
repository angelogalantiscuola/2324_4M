import json

def main():
    # Inizializzazione dei dati
    laboratori = {}
    prenotazioni = {}

    # Funzione per salvare i dati su un file JSON
    def salva_dati():
        with open('dati.json', 'w') as file:
            json.dump({'laboratori': laboratori, 'prenotazioni': prenotazioni}, file)

    # Funzione per caricare i dati da un file JSON
    def carica_dati():
        try:
            with open('dati.json', 'r') as file:
                data = json.load(file)
                laboratori.update(data['laboratori'])
                prenotazioni.update(data['prenotazioni'])
        except FileNotFoundError:
            pass

    # Funzione per aggiungere un laboratorio
    def aggiungi_laboratorio(id, nome, n_pcs):
        laboratori[id] = {'nome': nome, 'n_pcs': n_pcs}
        salva_dati()

    # Funzione per stampare laboratori disponibili
    def stampa_laboratori_disponibili():
        for lab_id, lab_info in laboratori.items():
            if lab_id not in prenotazioni:
                print(f"ID: {lab_id}, Nome: {lab_info['nome']}, Numero PC: {lab_info['n_pcs']}")

    # Funzione per cercare laboratori liberi in una certa fascia oraria
    def cerca_laboratori_liberi(orario):
        laboratori_liberi = []
        for lab_id, lab_info in laboratori.items():
            if lab_id not in prenotazioni:
                laboratori_liberi.append(lab_id)
        return laboratori_liberi

    # Funzione per aggiungere una prenotazione
    def aggiungi_prenotazione(lab_id, orario, classe, docente, materia):
        if lab_id in laboratori and lab_id not in prenotazioni:
            prenotazioni[lab_id] = {'orario': orario, 'classe': classe, 'docente': docente, 'materia': materia}
            salva_dati()
            return True
        return False

    # Funzione per rimuovere una prenotazione
    def rimuovi_prenotazione(lab_id):
        if lab_id in prenotazioni:
            del prenotazioni[lab_id]
            salva_dati()
            return True
        return False

    # Funzione per stampare il planning settimanale
    def stampa_planning_settimanale():
        giorni_settimana = ["lun", "mar", "mer", "gio", "ven"]
        orari = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]

        for lab_id, lab_info in laboratori.items():
            print(f"{lab_info['nome']}\n{' ' * 50}", end='')
            for giorno in giorni_settimana:
                for orario in orari:
                    prenotazione = prenotazioni.get(lab_id, None)
                    if prenotazione and prenotazione['orario'] == f"{giorno} - {orario}":
                        print(f"{prenotazione['classe']} {prenotazione['materia']} ({prenotazione['docente']}) | ", end='')
                    else:
                        print(" " * 50, end='')

                print()
            print()

    # Funzione per ripulire il planning settimanale
    def ripulisci_planning_settimanale():
        prenotazioni.clear()
        salva_dati()

    # Carica i dati al lancio del programma
    carica_dati()





    # Menu dell'applicativo
    while True:
        print("Menu:")
        print("1) Aggiungi laboratorio")
        print("2) Stampa laboratori disponibili")
        print("3) Cerca laboratori liberi in una certa fascia oraria")
        print("4) Aggiungi una prenotazione")
        print("5) Rimuovi una prenotazione")
        print("6) Stampa il planning settimanale")
        print("7) Ripulisci il planning settimanale")
        print("8) Esci")

        scelta = input("Inserisci il numero dell'operazione desiderata: ")

        if scelta == '1':
            lab_id = input("Inserisci l'ID del laboratorio: ")
            nome = input("Inserisci il nome del laboratorio: ")
            n_pcs = input("Inserisci il numero di PC: ")
            aggiungi_laboratorio(lab_id, nome, n_pcs)

        elif scelta == '2':
            stampa_laboratori_disponibili()

        elif scelta == '3':
            orario = input("Inserisci l'orario desiderato (es. lun 1st): ")
            laboratori_liberi = cerca_laboratori_liberi(orario)
            print("Laboratori liberi:", laboratori_liberi)

        elif scelta == '4':
            lab_id = input("Inserisci l'ID del laboratorio: ")
            orario = input("Inserisci l'orario della prenotazione (es. lun 1st): ")
            classe = input("Inserisci la classe: ")
            docente = input("Inserisci il docente: ")
            materia = input("Inserisci la materia: ")
            if aggiungi_prenotazione(lab_id, orario, classe, docente, materia):
                print("Prenotazione aggiunta con successo.")
            else:
                print("Impossibile aggiungere la prenotazione.")

        elif scelta == '5':
            lab_id = input("Inserisci l'ID del laboratorio da cui rimuovere la prenotazione: ")
            if rimuovi_prenotazione(lab_id):
                print("Prenotazione rimossa con successo.")
            else:
                print("Impossibile rimuovere la prenotazione.")

        elif scelta == '6':
            stampa_planning_settimanale()

        elif scelta == '7':
            ripulisci_planning_settimanale()

        elif scelta == '8':
            break

        else:
            print("Scelta non valida. Riprova.")