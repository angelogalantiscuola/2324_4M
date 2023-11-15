class Ascensore:
    def __init__(self,id_intero,piano_attuale,ultimo_piano,primo_piano,capienza_max,peso_max,n_persone):
        self.id_intero=id_intero
        self.piano_attuale=piano_attuale
        self.ultimo_piano=ultimo_piano
        self.primo_piano=primo_piano
        self.capienza_max=capienza_max
        self.peso_max=peso_max
        self.n_persone=n_persone
    def prenota(self):
        pren_piano=int(input(f"Inserisci il piano voluto:\n"))
        if self.n_persone<=self.capienza_max:
            if pren_piano>self.piano_attuale:
                diff=pren_piano-self.piano_attuale
                self.piano_attuale=self.piano_attuale+diff
                print(f"Il piano attuale e'{self.piano_attuale}")
            elif pren_piano==self.piano_attuale:
                print("Piano inserito è il piano attuale")
            else:
                diff=self.piano_attuale-pren_piano
                self.piano_attuale=self.piano_attuale-diff
                print(f"Il piano attuale e'{self.piano_attuale}")
        else:
            print("Si è superata la capienza massima e l'ascensore non funzionerà finchè non si libereranno dei posti")
ascensore1=Ascensore("10f",3,6,1,6,200,5)
ascensore1.prenota()
