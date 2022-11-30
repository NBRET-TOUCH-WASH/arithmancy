# ![onions have many layers](/docs/_assets/meta/logo/cromniomancy.png)<br>Character creation

After leaving the main menu via the new game creation option, players will enter a new segment: __character creation__. In this segment they will be able to create and customize a character to control while in *Arithmancy*'s environment.

---

## Fantasy Race selection

![race selection screenshot](/docs/_assets/pre/charCreation/race.png)<br>*A screenshot of the race selection screen as of `v0.1.0`.*

&nbsp;

On this screen, the player can select their character's __fantasy race__.

A fantasy race has a __name__, a __symbol__ representing the entities that belong to it, a relatively short __description__ and an ASCII artwork only made to look nice.

The main differences between races come from their __racial feats__, which kind of act like little boons and banes for a character. At the exception of the human race (*Cf.* *[§Human race](#human-race)*), the other two races both have advantages and disadvantages:

&nbsp;

### Human race

> #### No notable racial feats.

&nbsp;

### Dwarven race

> #### __[BOON]__ Cecity immunity
> 
> Character cannot be blinded by magical means.<br>Physical injuries and wounds to the eyes can however impact the character's sense of sight.

> #### __[BANE]__ Alcoholism
> 
> Character requires alcoholic beverages to remain sane, safe and sound.

&nbsp;

### Elven race

> #### __[BOON]__ Biological immortality
> 
> Character will not die of old age and only to violence and disease instead.

> #### __[BOON]__ Cuteness
> 
> Character is very cute.

> #### __[BANE]__ Protector of nature
> 
> Character is a devoted protector of nature due to their supernatural connection with it.<br>As such, they cannot use wooden items.

---

## Character Class selection

![class selection screenshot](/docs/_assets/pre/charCreation/class.png)<br>*A screenshot of the character class selection screen as of `v0.1.0`.*

&nbsp;

On this screen, the player can select their __character's class__.

A character class has a __name__, a __color__, a relatively short __description__ and an ASCII artwork only made to look nice.

Each class has different __attributes modifiers__, which change the character's statistics both in good or in bad:

&nbsp;

### Mage

|Attribute|Modifier value|
|:-:|:-:|
|`CON`|`-2`|
|`DEX`|`±0`|
|`INT`|`+3`|
|`STR`|`-3`|
|`WIS`|`±0`|

&nbsp;

### Necromancer

|Attribute|Modifier value|
|:-:|:-:|
|`CON`|`+1`|
|`DEX`|`±0`|
|`INT`|`+3`|
|`STR`|`-3`|
|`WIS`|`-1`|

&nbsp;

### Cleric

|Attribute|Modifier value|
|:-:|:-:|
|`CON`|`+1`|
|`DEX`|`-1`|
|`INT`|`-3`|
|`STR`|`-1`|
|`WIS`|`+3`|

&nbsp;

### Warrior

|Attribute|Modifier value|
|:-:|:-:|
|`CON`|`+2`|
|`DEX`|`+2`|
|`INT`|`-2`|
|`STR`|`+3`|
|`WIS`|`-2`|

---

## Attributes tweaking

![unchanged attribs tweaking screenshot](/docs/_assets/pre/charCreation/attribsDefault.png)<br>*A screenshot of an unchanged attributes tweaking screen as of `v0.1.0`.*

&nbsp;

On this screen, the player can tweak their character's __attributes__.

Attributes represent the character's aptitudes and abilities in different fields, such as spellcasting (`INT`, `WIS`), or physical nature (`CON`, `STR`).

&nbsp;

![changed attribs tweaking screenshot](/docs/_assets/pre/charCreation/attribsTweaked.png)<br>*A screenshot of an unchanged attributes tweaking screen as of `v0.1.0`.*

On this screen, on each line, can be found from left to right:

- The highlighted attribute's symbol (*e.g.* "`DEX`")
- The default value for any attribute (10)
- The currently modified attribute value
- The highlighted attribute's corresponding modifier

As indicated at the bottom of the screen (pictured above), the player can respectively increment or decrement an attribute's value with the *PLUS* and *MINUS* keys, spending a maximum of twenty (20) points.

Once done tweaking, an attribute's "final" value can be read as the equation presented on-screen; for example: __*`CON` = 10 + 4 – 2*__, which can be read as *"The value of the Constitution attribute equals ten plus four minus two"*, which when simplified equals 12.

&nbsp;

Once done with that, pressing the *RETURN* or keypad *ENTER* key will save the selected character data to a `.json` file and exit the character creation segment.