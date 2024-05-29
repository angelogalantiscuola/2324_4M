#inizio

class Student:

    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

class Classroom:

    def __init__(self, id, school_name, description):
        self.id = id
        self.school_name = school_name
        self.description = description
        self.students = []

    def add_student(self, student):
         self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)
    
    def count_enrolled_students(self):
        return len(self.students)

    
student1 = Student("Clausilio", "Concettini", "M", 61)

classroom = Classroom("ag43f67", "ISISS Gobetti", "Podologia")                                      # La Podologia si occupa di studiare tutte le patologie e le problematiche legate alla struttura e alla conformazione del piede. Inoltre, questa branca della Medicina si occupa della Diagnosi e del Trattamenti sanitario dei piedi e delle caviglie (Podologia), e se correlate ai piedi, anche delle patologie delle estremità inferiori delle gambe, finanche alla schiena (PodoPosturologia). La sua denominazione deriva dai termini dell’antico greco pous, podòs, che significa “piede” e logos, ou, che significa “ragione, discorso” ed è stato utilizzato per la prima volta negli Stati Uniti d’America nel Ventesimo secolo (Foot and Ankle Specialist o DPM Doctor Podiatric Medicine). È praticata dal Podologo[1], Dottore Specialista in Podologia, laurea inserita come branca della medicina riabilitativa riconosciuta in Italia dal Ministero della sanità in base al regolamento di cui al D.M. 666/1994 e norme successive.[2] Questo corso di studi è riconosciuto dallo Stato Italiano, e conferisce a chi lo termina la possibilità di operare in totale autonomia professionale. Alla facoltà di Podologia si può accedere dopo aver superato il test di accesso a numero chiuso. La laurea si conclude con l’abilitazione all’esercizio della professione di Podologo. Soprattutto negli ultimi anni, la Podologia sta avendo un notevole sviluppo in quanto gli odierni stili di vita comportano un aumentato rischio di contrarre patologie di interesse podologico. Si tratta di una professione con una grande proiezione nel futuro legata all’mportanza sempre più in crescita della salute dei nostri piedi. Il podologo esercita la sua professione sanitaria in tutte le fasce di età, con bambini, persone adulte, persone anzane, sportivi o persone che, per il loro lavoro, devono stare molto tempo in piedi. Oltre a questa sua ampia contemplazione di pazienti di tutte le età, la Podologia è suddivisa in ulteriori specialità peculiari: Podologia Pediatrica, Podologia Geriatrica, Podologia Sportiva, Podologia Diabetica, Podologia Reumatica, Podologia Angiologica, Podologia Neurologica. Podologia Pediatrica Fin dai primi anni di vita, il piede lavora in sinergia con il corpo per dare movimento e stabilità. È necessario quindi dare la giusta attenzione agli arti inferiori dei bambini per evitare la comparsa di patologie in età adulta. È infatti di grande importanza fare visite podologiche in età pediatrica, anche per evitare possibili problemi di deambulazione. La patologia più comune in età pediatrica è il piede piatto.

classroom.add_student(student1)                 # aggiunge uno studente al classroom

print("Number of enrolled students:", classroom.count_enrolled_students())      # conta quanti studenti ci sono nel classroom

classroom.remove_student(student1)          # rimuove uno studente dal classroom

print("Number of enrolled students:", classroom.count_enrolled_students())