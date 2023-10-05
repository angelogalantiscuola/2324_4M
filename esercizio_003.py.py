#1) crea un programma che legga la lista contenuta nel file JSON creato nel precedente esercizio e fornisca le seguenti funzionalità:
#-calcolo della rata del bollo per le auto contenute nella lista (formula: 2.58*kW(fino a 100kW) + 3.87(sui kW eccedenti))
#-calcolo dell'età media degli autoveicoli presenti nella lista

import json

def calcolaBollo (potenza_kW):
    if potenza_kW<=100:
        rata = potenza_kW * 2.58
    else:
        rata = 100*2.58 + (potenza_kW - 100) * 3.87 
    return float('%.2f' % rata)
    #return float(rata)

def calcolaEta(anno_produzione):
    return (2023-anno_produzione)



with open("cars.json","r") as f:
    cars = json.loads(f.read())

#print(type(cars))
#print(type(cars[0]))
#print(cars)

choice = int(input("Cosa vuoi fare?\n 1) calcola bollo\n 2) calcola età media parco auto\n"))

if choice==1:
    modello = input("Inserisci il modello: ")
    isPresent = False
    for temp in cars:
        if modello == temp["modello"]:
            isPresent = True 

    if isPresent == True:
        for temp in cars:
            if temp["modello"]==modello:
                print("La rata del bollo è", calcolaBollo(temp["potenza_kW"]))
                #bollo = calcolaBollo(temp["potenza_kW"])
                #print(f"La rata del bollo è {bollo:.2f}") #formattazione con f-string     
    else:
        print("Modello non presente!!!")

elif choice==2:
    eta=0
    for temp in cars:
        eta+=calcolaEta(temp["anno_produzione"])

    eta_media=eta/len(cars)
    print("l'età media del parco auto è", eta_media,"anno/i")

else:
    print("opzione non valida")
