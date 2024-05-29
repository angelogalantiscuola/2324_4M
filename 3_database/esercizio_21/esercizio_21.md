# Sistema di Gestione di un Negozio di Musica

## Descrizione dell'Esercizio

L'obiettivo di questo esercizio è progettare un'applicazione Python utilizzando classi e un database per modellare un sistema di gestione di un negozio di musica. Il sistema dovrebbe includere tre entità principali: `Negozio`, `Cliente` e `Album`.

## Requisiti Dettagliati

1. Classe `Negozio`: 
    - Questa classe dovrebbe avere un attributo che rappresenta il nome del negozio e un altro attributo che rappresenta il numero di album disponibili. 
    - Dovrebbe anche includere un metodo per visualizzare gli album disponibili.

2. Classe `Cliente`: 
    - Questa classe dovrebbe avere un attributo che rappresenta il nome del cliente e un altro attributo che rappresenta il cognome del cliente. 
    - Dovrebbe anche includere un metodo per visualizzare il nome completo del cliente.

3. Classe `Album`: 
    - Questa classe dovrebbe avere un attributo che rappresenta il titolo dell'album, un altro attributo che rappresenta l'artista dell'album e un attributo `codice_a_barre` univoco.
    - Dovrebbe anche includere un metodo per visualizzare il titolo, l'artista e il codice a barre dell'album.

4. Database: 
    - Crea un database che include le tabelle `Negozio`, `Cliente` e `Album`. 
    - Stabilisci relazioni appropriate tra le tabelle e crea classi Python corrispondenti per interagire con il database.

Le relazioni tra le tabelle dovrebbero essere le seguenti:

- Un cliente può acquistare più album e un album può essere acquistato un solo cliente.
- Un negozio può avere molti clienti e un cliente può acquistare da molti negozi.