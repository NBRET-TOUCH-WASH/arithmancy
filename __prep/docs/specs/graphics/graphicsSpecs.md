# ![layerzzzzz](/__prep/docs/assets/cromniomancy.png)

Specifications for the __graphics__ in *Arithmancy*.

At the time of writing, colors from preparatory images/sketches are __not__ to be taken into account.

### Contents
- [Global specifications](#global-specifications)
    - [Resolution](#resolution)
    - [Standardized colors](#standardized-colors)
    - [Character set](#character-set)
- [Main menu](#main-menu)
- [Main game](#main-game)
- [Game Over screen](#game-over-screen)

---

## Global specifications

This section focuses on graphics settings that apply to every aspect of the game.

### Resolution

The game's resolution is not specified in pixels (`px`), rather, it is specified in *COLUMNS* and *LINES*, manipulated according to a ![coordinates](/__prep/docs/assets/graphics/coordinates.png) coordinate system.

- Resolution (*COLUMNS*x*LINES*): `115x65`
    - Width (*COLUMNS*) : `115`
    - height (*LINES*): `65`

&nbsp;

### Standardized colors

*Airthmancy* uses a set of standardized colors ~~totally not taken from *Dwarf Fortress*~~:

|Color|Hex code|RGB format|
|-:|:-|:-|
|*Black*|`#000000`|`(0,0,0)`|
|*Dark Blue*|`#000080`|`(0,0,128)`|
|*Light Blue*|`#0000ff`|`(0,0,255)`|
|*Brown*|`#808000`|`(128,128,0)`|
|*Dark Gray*|`#808080`|`(128,128,128)`|
|*Light Gray*|`#c0c0c0`|`(192,192,192)`|
|*Lime*|`#00ff00`|`(0,255,0)`|
|*Green*|`#008000`|`(0,128,0)`|
|*Purple*|`#800080`|`(128,0,128)`|
|*Red*|`#ff0000`|`(255,0,0)`|
|*Teal*|`#008080`|`(0,128,128)`|
|*White*|`#ffffff`|`(255,255,0)`|*Yellow*|`#ffff00`|`(255,255,0)`|

&nbsp;

### Character set

Much in the tradition of original [roguelikes](https://en.wikipedia.org/wiki/Roguelike) and [TUIs](https://en.wikipedia.org/wiki/Text-based_user_interface), the game uses ASCII characters in order to visualize its different elements, as such, each character needs to symbolize a specific things, dependant (or not) of the context:

|Character|Usage|Remarks|
|:-|-:|:-|
|`@`|Player character||
|`☺`|||
|`☻`|||
|`e`|||
|`g`|||
|`Ω`|Blob|*Can appear in different colors*|
|`¥`|Skeleton||
|`♣`|Tree||
|`♠`|Bush||

---

## Main menu

The main menu for the game, which will greet player upon execution:

![mainMenu](/__prep/docs/assets/graphics/mainMenu.png)

This appearance was essentially inspired by two games:

- *Dwarf Fortress*' main menu:

![dwarfFortressMainMenu](/__prep/docs/assets/graphics/dwarfFortressMainMenu.png)

- *Yume Nikki*'s main menu (and basically a lot of other *RPG Maker* games):

![yumeNikkiMainMenu](/__prep/docs/assets/graphics/YumeNikkiMainMenu.jpg)

---

## Main game

During the main part of the game, the UI should look something like this:

![main game sketch](/__prep/docs/assets/graphics/mainGame.png)

This screen layout is inspired by several games:

- *Dwarf Fortress*' __Adventure[r] mode__ main screen:

![dwarFortressMainGame](/__prep/docs/assets/graphics/dwarfFortressMainGame.png)

- *Angband*'s main screen:

![angbandMainGame](/__prep/docs/assets/graphics/angbandMainGame.png)

- This untiltled Open World RPG gamemade with `curses` by [Kibble](https://www.youtube.com/channel/UCV0ZS4chB5X1oR0Nz_WtdzQ):

![angbandMainGame](/__prep/docs/assets/graphics/kibbleGameMainGame.jpg)

---

## Game Over screen

The Game Over screen, appearing upon player death:

![gameOver](/__prep/docs/assets/graphics/gameOver.png)

Layout inspired by:

- *Angband*'s Game Over screen/menu:

![angbandGameOver](/__prep/docs/assets/graphics/angbandGameOver.png)

- *Shadowgate*'s Game Over sequence:

![shadowgateGameOver](/__prep/docs/assets/graphics/shadowgateGameOver.png)