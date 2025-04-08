```mermaid
classDiagram
    class Game
    class Level
    class Player
    class Box
    class Laser
    class pygame_sprite_Sprite

    Game *-- Level
    Game *-- Player
    Game *-- Box
    Game *-- Laser

    Player --|> pygame_sprite_Sprite
    Box --|> pygame_sprite_Sprite
    Laser --|> pygame_sprite_Sprite

    Game ..> Level
    Game ..> Player
    Game ..> Box
    Game ..> Laser