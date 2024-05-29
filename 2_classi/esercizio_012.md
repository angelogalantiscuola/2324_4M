Questo esercizio riguarda la creazione di una gerarchia di classi per rappresentare diversi tipi di libri.

- **Book**: Questa è la classe base che rappresenta un libro generico. Ha tre metodi: 
    - `leggi`: stampa un messaggio che indica che stai iniziando a leggere il libro. 
    - `segna_pagina`: prende un numero di pagina come input e stampa un messaggio che indica che hai segnato quella pagina nel libro. 
    - `descrivi`: stampa il titolo e l’autore del libro.

- **Novel**: Questa classe eredita dalla classe `Book` e aggiunge un attributo `genere`. Ha un metodo aggiuntivo `ottieni_genere` che restituisce il genere del romanzo. 
Il metodo `descrivi` è sovrascritto per includere anche il genere nella descrizione.

- **ScienceFiction** e **Fantasy**: Queste classi ereditano entrambe dalla classe `Novel`. 
    - `ScienceFiction`: aggiunge un attributo `tecnologia_futuristica` e un metodo `ottieni_tecnologia_futuristica` che restituisce la tecnologia futuristica del libro. 
    - `Fantasy`: aggiunge un attributo `sistema_magico` e un metodo `ottieni_sistema_magico` che restituisce il sistema magico del libro.

Infine, vengono creati e utilizzati oggetti di ciascuna classe. Per ogni libro, si inizia a leggere, si segna una pagina e si descrive il libro. Per i romanzi, si ottiene anche il genere. Per i libri di fantascienza, si ottiene anche la tecnologia futuristica. Per i libri fantasy, si ottiene anche il sistema magico.