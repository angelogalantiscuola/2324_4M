# Esercizio 6: Automatizzazione delle prenotazioni dei laboratori

Una scuola superiore vuole semplificare il processo di prenotazione settimanale per i suoi laboratori. Per fare ciò, ha commissionato alla classe 4M lo sviluppo di una soluzione software.

L'applicativo dovrà prevedere un menù con le seguenti funzionalità:

1. Aggiungi laboratorio (id/nome, n_pcs)
2. Stampa laboratori disponibili
3. Cerca laboratori liberi in una certa fascia oraria (es. prima e seconda ora)
4. Aggiungi una prenotazione (classe, docente, materia)
5. Rimuovi una prenotazione
6. Stampa il planning settimanale per ogni laboratorio su un file di testo
7. Ripulisci il planning settimanale

L'applicativo dovrà essere sviluppato utilizzando le conoscenze sui dizionari/liste e sui file JSON in linguaggio Python.

Nota bene:
- Garantire la memorizzazione dei dati di prenotazione su un file JSON
- Gestire le ore come meglio si crede (1st, 2nd, 3..... 8.00-9.00, 9.00-10.00....)
- Per semplificare, gestire il planning di una sola settimana