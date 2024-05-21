# Sistema di Gestione del Garage

## Descrizione dell'Esercizio

L'obiettivo di questo esercizio è progettare un'applicazione Python utilizzando classi e un database per modellare un sistema di gestione del garage. Il sistema dovrebbe includere tre entità principali: `Garage`, `Cliente` e `Auto`.

## Requisiti Dettagliati

1. Classe `Garage`: 
   - Questa classe dovrebbe avere un attributo che rappresenta il nome del garage e un altro attributo che rappresenta il numero di posti auto disponibili. 
   - Dovrebbe anche includere un metodo per visualizzare i posti auto disponibili.

2. Classe `Cliente`: 
   - Questa classe dovrebbe avere un attributo che rappresenta il nome del cliente e un altro attributo che rappresenta il cognome del cliente. 
   - Dovrebbe anche includere un metodo per visualizzare il nome completo del cliente.

3. Classe `Auto`: 
   - Questa classe dovrebbe avere un attributo che rappresenta la targa dell'auto e un altro attributo che rappresenta il modello dell'auto. 
   - Dovrebbe anche includere un metodo per visualizzare la targa e il modello dell'auto.

4. Database: 
   - Crea un database che include le tabelle `Garage`, `Cliente` e `Auto`. 
   - Stabilisci relazioni appropriate tra le tabelle e crea classi Python corrispondenti per interagire con il database.

Le relazioni tra le tabelle dovrebbero essere le seguenti:

- Un cliente può possedere più auto, ma un'auto può appartenere solo a un cliente.
- Un garage può ospitare più auto, ma un'auto può essere solo in un garage alla volta (considera che un'auto può essere solo in un garage alla volta, non vogliamo modellare la storia delle auto in un garage).