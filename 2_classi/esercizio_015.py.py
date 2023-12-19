class Studente:
    def __init__(self, nome, cognome, genere, eta):
        self.nome = nome
        self.cognome = cognome
        self.genere = genere
        self.eta = eta
        self.corsi_iscritti = []

    def __str__(self):
        return f"{self.nome} {self.cognome}"

    def iscrivi_corso(self, corso):
        self.corsi_iscritti.append(corso)
        corso.add_studente(self)

class Corso:
    def __init__(self, corso_id, uni_name, descrizione):
        self.corso_id = corso_id
        self.uni_name = uni_name
        self.descrizione = descrizione
        self.elenco_studenti_iscritti = []

    def __str__(self):
        return f"Corso {self.corso_id} - {self.uni_name}"

    def add_studente(self, studente):
        self.elenco_studenti_iscritti.append(studente)

    def remove_studente(self, studente):
        self.elenco_studenti_iscritti.remove(studente)

    def studenti_iscritti_count(self):
        return len(self.elenco_studenti_iscritti)

    def studenti_iscritti_elenco(self):
        return [str(studente) for studente in self.elenco_studenti_iscritti]

# Esempio di utilizzo:

# Creazione di studenti
studente1 = Studente("Mario", "Rossi", "M", 20)
studente2 = Studente("Anna", "Bianchi", "F", 22)

# Creazione di corsi
corso1 = Corso("C001", "Università X", "Introduzione a Python")
corso2 = Corso("C002", "Università Y", "Programmazione avanzata")

# Iscrizione degli studenti ai corsi
studente1.iscrivi_corso(corso1)
studente1.iscrivi_corso(corso2)
studente2.iscrivi_corso(corso2)

# Visualizzazione degli studenti iscritti a ciascun corso
print(f"{corso1} - Studenti iscritti: {corso1.studenti_iscritti_elenco()}")
print(f"{corso2} - Studenti iscritti: {corso2.studenti_iscritti_elenco()}")

# Visualizzazione dei corsi a cui è iscritto uno studente
print(f"{studente1} - Corsi iscritti: {[str(corso) for corso in studente1.corsi_iscritti]}")
print(f"{studente2} - Corsi iscritti: {[str(corso) for corso in studente2.corsi_iscritti]}")
