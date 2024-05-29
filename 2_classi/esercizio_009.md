# Implementazione della Classe Ascensore

Implementa una classe che modella il funzionamento di un ascensore. Le caratteristiche dell'ascensore sono le seguenti:

- Un ID intero
- Piano attuale (intero)
- Ultimo piano e primo piano (intero)
- Capienza massima (intero)
- Peso massimo (float)

Le funzionalità sono:
- `prenota()`
- `sali()`
- `scendi()`

Prima di avviare una salita o una discesa, assicurati che:

1. Il numero di persone e il peso combinato non superino i massimi consentiti.
2. Il numero di piani che si vuole salire o scendere non superi il numero di piani dell'edificio o non scenda sotto il primo (il primo piano può essere negativo in caso di piani interrati).