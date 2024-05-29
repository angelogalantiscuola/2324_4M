# Esercizio 3

Questo esercizio richiede di creare un programma Python che esegue le seguenti operazioni:

1. Legge la lista di automobili contenuta nel file JSON.
2. Calcola la rata del bollo per le auto contenute nella lista. La formula per il calcolo è: `2.58 * kW (fino a 100kW) + 3.87 (sui kW eccedenti)`.
3. Calcola l'età media degli autoveicoli presenti nella lista.

## Esempio

Supponiamo che il file JSON contenga i dati per due automobili come segue:

```json
[
    {
        "Marca": "Ferrari",
        "Modello": "488 GTB",
        "Anno di produzione": 2015,
        "Potenza": 670
    },
    {
        "Marca": "Lamborghini",
        "Modello": "Huracan",
        "Anno di produzione": 2014,
        "Potenza": 610
    }
]
```