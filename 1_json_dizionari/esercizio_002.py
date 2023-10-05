#Baffert Alexander
import json
import numpy as np
n=np.array([])
lista_di_auto=[]
#creazione dizionario
for i in range(2):
    marcaa=input("Inserire la marca dell'auto: ")
    modelloo=input("Inserire il modello dell'auto: ")
    annop=int(input("Inserire l'anno di produzione: "))
    cavalli=int(input("Inserire la potenza: "))
    #inserimento di dati  
    lista_di_auto.append(dict(marca=marcaa,modello=modelloo,anno=annop,potenza=cavalli))
with open("b.json","w")as f:
    f.write(json.dumps(lista_di_auto))