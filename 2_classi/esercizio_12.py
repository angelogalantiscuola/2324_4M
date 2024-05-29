#Classe Book
class Book:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def leggi(self):
        print(f"Inizi a leggere {self.titolo}.")

    def segna_pagina(self, numero_pagina):
        print(f"Pagina {numero_pagina} segnata in {self.titolo}.")

    def descrivi(self):
        print(f"Titolo: {self.titolo}\nAutore: {self.autore}")

#Classe Novel
class Novel(Book):
    def __init__(self, titolo, autore, genere):
        super().__init__(titolo, autore)
        self.genere = genere

    def ottieni_genere(self):
        return self.genere

    def descrivi(self):
        super().descrivi()
        print(f"Genere: {self.genere}")

#Classe ScienceFiction
class ScienceFiction(Novel):
    def __init__(self, titolo, autore, genere, tecnologia_futuristica):
        super().__init__(titolo, autore, genere)
        self.tecnologia_futuristica = tecnologia_futuristica

    def ottieni_tecnologia_futuristica(self):
        return self.tecnologia_futuristica

    def descrivi(self):
        super().descrivi()

#Classe Fantasy
class Fantasy(Novel):
    def __init__(self, titolo, autore, genere, sistema_magico):
        super().__init__(titolo, autore, genere)
        self.sistema_magico = sistema_magico

    def ottieni_sistema_magico(self):
        return self.sistema_magico

    def descrivi(self):
        super().descrivi()

# Creazione e utilizzo di oggetti delle varie classi
Book = Book("Veri Amici", "I Mates")
Book.leggi()
Book.segna_pagina(100)
Book.descrivi()

Novel = Novel("1984", "George Orwell", "Political fiction novel")
print("\ndescrizione del Romanzo:")
Novel.leggi()
Novel.segna_pagina(100)
Novel.descrivi()
print(f"Genere: {Novel.ottieni_genere()}") 

ScienceFiction = ScienceFiction("Akira", "Katsuhiro Otomo", "Dystopian", "Weapons")
print("\ndescrizione Fantascienza:")
ScienceFiction.leggi()
ScienceFiction.segna_pagina(100)
ScienceFiction.descrivi()
print(f"Genere: {ScienceFiction.ottieni_genere()}") 
print(f"Tecnologia Futuristica: {ScienceFiction.ottieni_tecnologia_futuristica()}")

fantasy = Fantasy("Il Trono di Spade", "George R. R. Martin", "Fantasy", "Dragons")
print("\ndescrizione Fantasy:")
fantasy.leggi()
fantasy.segna_pagina(100)
fantasy.descrivi()
print(f"Genere: {fantasy.ottieni_genere()}") 
print(f"Sistema Magico: {fantasy.ottieni_sistema_magico()}")