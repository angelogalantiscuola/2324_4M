# Esercizio 2

Questo esercizio richiede di creare un programma Python che esegue le seguenti operazioni:

1. Chiede all'utente di inserire i dati per un numero specifico di automobili. I dati per ogni automobile dovrebbero includere dettagli come marca, modello, anno di produzione, ecc.
2. Aggiunge i dati di ogni automobile a una lista di dizionari, dove ogni dizionario rappresenta un'automobile.
3. Salva la lista di dizionari in un file JSON per la persistenza dei dati.

## Esempio

Supponiamo che l'utente inserisca i dati per due automobili. Il programma potrebbe funzionare come segue:

```python
# L'utente inserisce i dati per la prima automobile
Marca: "Ferrari"
Modello: "488 GTB"
Anno di produzione: 2015

# L'utente inserisce i dati per la seconda automobile
Marca: "Lamborghini"
Modello: "Huracan"
Anno di produzione: 2014

# Il programma salva i dati in un file JSON
[
    {
        "Marca": "Ferrari",
        "Modello": "488 GTB",
        "Anno di produzione": 2015
    },
    {
        "Marca": "Lamborghini",
        "Modello": "Huracan",
        "Anno di produzione": 2014
    }
]
```