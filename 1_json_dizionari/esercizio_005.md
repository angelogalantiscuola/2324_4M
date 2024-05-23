# Creazione di un'applicazione per la gestione del catalogo di un museo

L'obiettivo di questo esercizio è realizzare un'applicazione che utilizza dizionari, liste e file JSON per gestire il catalogo di un museo. L'applicazione dovrà fornire le seguenti funzionalità:

1) Consultare le stanze presenti nel museo.
2) Cercare informazioni su un'opera specifica.
3) Cancellare un'opera dal catalogo.
4) Cancellare una stanza solo se è vuota.

**Nota Bene:** Ad ogni modifica del catalogo, l'applicazione dovrà aggiornare il file JSON per garantire la persistenza dei dati. L'applicazione dovrà inoltre presentare un menù numerato che elenca le varie funzionalità.

## Esempio

Supponiamo di avere un museo con due stanze. La prima stanza contiene l'opera "La Gioconda", mentre la seconda stanza è vuota. L'applicazione dovrà permettere di visualizzare queste informazioni, cercare dettagli sull'opera "La Gioconda", rimuovere "La Gioconda" dal catalogo e, infine, cancellare la seconda stanza dal museo poiché è vuota.

```python
# Progettare la struttura dati a priori in modo da garantire le funzionalità richieste.
 museo = {
     "nome": "Museo di Roma",
     "stanze": [],
 }

 stanza = {
     "nome": "Rinascimento",
     "opere": [],
 }

 opera = {
     "titolo": "La creazione di Adamo",
     "artista": "Michelangelo",
     "anno": 1512,
 }
```