# Classi e Oggetti

Creare una classe `Auto` con i seguenti attributi: `marca`, `modello`, `targa` e `km_percorsi`. 

Il costruttore `__init__()` dovrebbe permettere di istanziare un nuovo oggetto `Auto` con i valori specificati per questi attributi.

Inoltre, la classe dovrebbe avere un metodo `effettua_viaggio(km)` che aggiunge i chilometri specificati all'attributo `km_percorsi`.

Ecco un esempio di come potrebbe essere strutturata la classe:

```
@startuml
class Auto{
  marca : string
  modello : string
  km : int
  anno : int
  --
  constructor(marca : string, modello : string, km : int, anno : int)
  effettua_viaggio (km: int) : int
  get_anno() : int
  set_anno(anno: int) : bool
}
@enduml
```