```mermaid
classDiagram
    Player o-- Warrior

    class Player {
        +string Name
        +string Gender

        +int hp
        +int mp


        +Move()
        +virtual Attack()
        +Drinky()
    }

    class Warrior {
        +override Attack()
    }
```