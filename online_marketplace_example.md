# Driving Scenario

## Narrative version

In our world, we have individuals, each with a unique name and age. These individuals, or 'Persons' as we call them, have the ability to drive cars.

Cars, each distinct with a make, model, and year of manufacture, are the vessels that our Persons use to navigate their world. These Cars are not exclusive to one Person. In fact, they can be driven by many different Persons.

Similarly, a Person is not limited to driving just one Car. They have the freedom to drive many Cars, experiencing the unique characteristics each Car has to offer. This creates a dynamic and interconnected world of Persons and Cars.

## Technical version

1. We have a `Person` who can `drive` a `Car`. The `Person` has a `name` and `age`.

2. Each `Car` can be driven by a `Person`. The `Car` has a `make`, `model`, and `year`.

3. A `Person` can drive many `Cars`, and each `Car` can be driven by many `Persons`.

## UML version

``` plantuml
@startuml example

class Person {
    +name: String
    +age: Number
    +drive(car: Car): void
}

class Car {
    +make: String
    +model: String
    +year: Number
}

Person "many" -- "many" Car : drives >

@enduml
```
