# Garage

## Testo esercizio

Si vuole realizzare un applicativo che permetta di modellare mediante classi Python e un database la gestione di un garage. Si consideri una classe Garage, un Cliente e un Auto.

## Dettaglio di una possibile soluzione

La classe Garage deve avere un attributo che rappresenta il nome del garage e un attributo che rappresenta il numero di posti auto disponibili. Deve inoltre avere un metodo che permetta di visualizzare i posti auto disponibili.

La classe Cliente deve avere un attributo che rappresenta il nome del cliente e un attributo che rappresenta il cognome del cliente. Deve inoltre avere un metodo che permetta di visualizzare il nome e il cognome del cliente.

La classe Auto deve avere un attributo che rappresenta la targa dell'auto e un attributo che rappresenta il modello dell'auto. Deve inoltre avere un metodo che permetta di visualizzare la targa e il modello dell'auto.

Si crei un database che contenga le tabelle Garage, Cliente e Auto. Si creino le opportune relazioni tra le tabelle. Si creino le opportune classi Python che permettano di interagire con il database.

La relazione tra le tabelle deve essere la seguente:

- Un cliente può avere più auto, un auto può essere di un solo cliente
- Un garage può avere più auto, un auto può essere in un solo garage (si consideri che un auto può essere in un solo garage alla volta, non si vuole modellare lo storico delle auto in un garage)
