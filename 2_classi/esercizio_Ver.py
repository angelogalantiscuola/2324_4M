class Persona:
    def __init__(self,id:str,nome:str,cognome:str,contatto:str) -> None:
        self.id=id
        self.nome=nome
        self.cognome=cognome
        self.contatto=contatto
    def __str__(self) -> str:
        return f"Persona(id: {self.id},nome: {self.nome},cognome: {self.cognome},contatto: {self.contatto})"

class Volo:
    def __init__(self,n_volo:str,aeroporto_partenza:str,aeroporto_arrivo:str,dataora_partenza:str,posti_disponibili:int) -> None:
        self.n_volo=n_volo
        self.aeroporto_partenza=aeroporto_partenza
        self.aeroporto_arrivo=aeroporto_arrivo
        self.dataora_partenza=dataora_partenza
        self.posti_disponibili=posti_disponibili
    def __str__(self) -> str:
        return f"Volo(n_volo: {self.n_volo},aeroporto partenza: {self.aeroporto_partenza},aeroporto arrivo: {self.aeroporto_arrivo},data ora partenza:{self.dataora_partenza},posti disponibili: {self.posti_disponibili})"
    def Disponibilita(self):
        return self.posti_disponibili>0

class Prenotazione:
    def __init__(self,id_pren:str,passeggero:object,volo:object,dataora_partenza:str,stato_pren:str,importo:float) -> None:
        self.id_pren=id_pren
        self.passeggero=passeggero
        self.volo=volo
        self.dataora_partenza=dataora_partenza
        self.stato_pren=stato_pren
        self.importo=importo
    def CambiaNominativo(self, passeggero):
        self.passeggero=passeggero
        return "Passeggero cambiato correttamente!"
    def __str__(self) -> str:
        return f"Prenotazione(id prenotazione: {self.id_pren}, passeggiero: {self.passeggero},volo: {self.volo},dataora partenza: {self.dataora_partenza},stato prenotazione: {self.stato_pren},importo: {self.importo})"
    

class Passeggero(Persona):
    def __init__(self, id: str, nome: str, cognome: str, contatto: str) -> None:
        super().__init__(id, nome, cognome, contatto)
        self.lista_prenotazioni=[]
        self.punti_fedelta=0
        self.n_prenotazioni=0
    def __str__(self) -> str:
        return f"Persona(id: {self.id},nome: {self.nome},cognome: {self.cognome},contatto: {self.contatto},punti fedelta': {self.punti_fedelta})"
    def PrenotaVolo(self, volo: Volo, importo: float)->Prenotazione:
        if volo.Disponibilita():
            id=str(self.id)+"_"+str(self.n_prenotazioni)
            self.n_prenotazioni=self.n_prenotazioni+1
            volo.posti_disponibili=volo.posti_disponibili-1
            prenotazione=Prenotazione(id,self,volo,volo.dataora_partenza,"Prenotato",importo)
            self.lista_prenotazioni.append(prenotazione)
            print("Prenotazione effettuata!")
            return prenotazione
        else:
            print ("Posti esauriti!")
            return None

        self.lista_prenotazioni.append(Prenotazione)
        return "Prenotazione effettuata!"
    def CancellaVolo(self,prenotazione):
        if prenotazione in self.lista_prenotazioni:
            self.lista_prenotazioni.remove(prenotazione)
            return "Cancellazione prenotazione effettuata!"
        else:
            return "Prenotazione inesistente."
    def AggiornamentoPunti(self,punti):
        self.punti_fedelta=self.punti_fedelta+punti
        return "Aggiornamento punti effettuato!"
class PasseggeroBusiness(Passeggero):
    def __init__(self, id: str, nome: str, cognome: str, contatto: str, nome_azienda: str, sconto_azienda: float) -> None:
        super().__init__(id, nome, cognome, contatto)
        self.nome_azienda=nome_azienda
        self.sconto_azienda=sconto_azienda
    def __str__(self) -> str:
        return f"Persona(id: {self.id},nome: {self.nome},cognome: {self.cognome},contatto: {self.contatto},prenotazioni: {self.lista_prenotazioni},punti fedelta': {self.punti_fedelta},nome azienda: {self.nome_azienda},sconto: {self.sconto_azienda})"
    def ApplicaSconto(self, importo: float)->float:
        return importo-(importo*self.sconto_azienda)
class Staff(Persona):
    def __init__(self, id: str, nome: str, cognome: str, contatto: str, id_staff: str,ruolo: str) -> None:
        super().__init__(id, nome, cognome, contatto)
        self.id_staff=id_staff
        self.ruolo=ruolo
        self.turni=[]
    def __str__(self) -> str:
        return f"Persona(id: {self.id},nome: {self.nome},cognome: {self.cognome},contatto: {self.contatto},id staff: {self.id_staff},ruolo: {self.ruolo})"
    def AggiungiVolo(self,volo):
        self.turni.append(volo)
        return "Il volo è stato inserito correttamente!"
    def CancellaVolo(self,volo):
        if volo in self.turni:
            self.turni.remove(volo)
            return "Volo cancellato correttamente!"
        else:
            return "Volo inesistente."

#main    
pippi=Persona("h1","pippi","mhanz","12344321")
print("pippi:\n",pippi)

pippi1=Passeggero("h2","pippi","mhanz","12344321")
print("pippi1:\n",pippi1)


volo_pippis=Volo("1034","francoforte","fortefranco","11-09-2001",35)
print("volo_pippis:\n",volo_pippis)
print("")

prenotazione1=pippi1.PrenotaVolo(volo_pippis,326.87)
print("Prenotazione1:\n",prenotazione1)




print(pippi1.CancellaVolo(pippi1.lista_prenotazioni[0]))
print(pippi1.AggiornamentoPunti(7))

pippi2=PasseggeroBusiness("h","pippi","mhanz","12344321","pippi and co.",0.1)
prenotazione2=pippi2.PrenotaVolo(volo_pippis,420.87)

print("Prezzo",prenotazione2.passeggero.ApplicaSconto(prenotazione2.importo))

pippi3=Staff("h3","pippi","mhanz","12344321","g5g6","lavatoilette")
print(pippi3.AggiungiVolo(volo_pippis))
print(pippi3.CancellaVolo(volo_pippis))
print(volo_pippis.Disponibilita())

pippi4=Passeggero("h4","pippi4","mhanz4","12344321")

pippi2.CancellaVolo(prenotazione2)
prenotazione2.CambiaNominativo(pippi4)
print(prenotazione2)