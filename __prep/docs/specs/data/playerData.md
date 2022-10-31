# ![onionos bananos](/__prep/docs/assets/cromniomancy.png)

Data specifications for the __player character__ in *Arithmancy*.

### Contents
- [Biography](#biography)
    - [Name](#name)
    - [Gender](#gender)
- [Race](#race)
    - [Racial feats](#racial-feats)
- [Class](#class)
    - [Title](#title)
        - [Mage](#mage)
        - [Necromancer](#necromancer)
        - [Priest](#priest)
        - [Warrior](#warrior)
- [Traits](#traits)
- [Subsistence gifts](#subsistence-gifts)
- [Status effects](#status-effects)
    - [Acid-splattered](#acid-splattered-acid)
    - [Ablaze](#ablaze-blaz)
    - [Blessed](#blessed-bles)
    - [Blind](#blind-blnd)
    - [Frozen](#frozen-froz)
    - [Hexed](#hexed-hexd)
    - [Poisoned](#poisoned-pois)
---

## Biography

Data related to the player character's information, identity, lore elements and maybe much more...

&nbsp;

### Name

The player character's name.

Can be __chosen and manually typed in__ by the player or __taken at random__ from a set of name databases.

&nbsp;

### Gender

The player character's gender.

Can be __taken from a set of prewritten genders__ or __manually typed in__ by the player.

---

## Race

Data related to the player character's (fantasy) race.

Here, *"race"* does not designate the character's [complexion](https://en.wikipedia.org/wiki/Human_skin_color). Instead, it simply designates the race of creatures the character belongs to, including but not limited to:

|Race|Symbol(s)|Demonym|Remarks|
|:-|:-:|:-:|:-|
|Human|`U`, `Ü` ...|__*sg.*__ *Human*<br>__*pl.*__ *Humans*||
|Dwarven|`☺`, `☻`|__*sg.*__ *Dwarf*<br>__*pl.*__ *Dwarves*||
|Elven|`e`, `ê` ...|__*sg.*__ *Elf*<br>__*pl.*__ *Elves*||
|Goblins|`g`|__*sg.*__ *Elf*<br>__*pl.*__ *Elves*||

&nbsp;

### Racial feats

With each race come advantages and drawbacks, categorized under the term *"racial feats"*. These feats can influence the character's [traits](#traits) both in good or in bad, and force [a certain balance](https://en.wiktionary.org/wiki/falsehood#English) between the game's different races.

These feats are detailed below according to the following structure:

|Feat|Description|Remarks|
|:-:|-:|:-|
|*Berserker*|Character gives into a trance-like __fury__|Temporarily __increases__ `STR`, `SPD`.<br>Temporarily __decreases__ `INT`, `WIS`.|
|*TODO*|__TODO__|TODO|

---

## Class

> In role-playing games (RPGs), character classes aggregate several abilities and aptitudes, and may also detail aspects of background and social standing, or impose behavior restrictions.<br>Classes may be considered to represent archetypes, or specific careers.
> 
> #### [Wikipedia](https://en.wikipedia.org/wiki/Character_class)

&nbsp;

The different character classes available in-game include:

<!-- § make this better than a shitty table -->

|Class|Features|Remarks|
|:-:|:-|:-|
|*Mage*|¤ Learns __Arcane magic__<br>¤ Uses it to __cast spells__ of their choice|While obviously skillful when it comes to magical prowesses, mages are often observed to lack some of the physical strength observed in some other classes.|
|*Necromancer*|¤ Learns __Black magic__<br>¤ Uses it to __cast spells__ of their choice|Differs from the _Mage_ and _Priest_ in the type of magic they are versed into.|
|*Priest*|¤ Learns __White magic__<br>¤ Uses it to __cast spells__ of their choice|Differ from the _Mage_ and _Necromancer_ in the type of magic they are versed into.|
|*Warrior*|¤ __Does not use magic__<br>¤ Relies on their __raw strength__ and physical aptitudes|While merciless at combat, warriors generally lack the abilities to perform litterary feats and spellwork due to their lack of magical education.|

&nbsp;

### Title

Each class possesses a set of __titles__. Not all characters bear a title, however when they do, it generally represents their level of skill and mastery of their class' aptitudes and abilities.

Titles can alternatively be referred to as a *"skill level"*, differing although correlated to the character's *experience level* (also named *rank*) .

Class titles go as follows:

&nbsp;

#### Mage

|Rank|Title|Remarks|Origin/Reference/Inspiration|
|:-:|:-:|:-|:-:|
|`0`|*Judge*|__Unused__ (automatically incremented).<br>Used for debugging purposes.|Occult tarot __(Judgement ⅩⅩ)__|
|`1`|*Scholar*||≈ *Dark Souls Ⅱ*|
|`2`|*Preceptor*||≈ *Dwarf Fortress*|
|`3`|*Harbinger*||*Warhammer 40,000*|
|`4`|*Oracle of Change*||″|
|`5`|*Demigod*||Theology|
|`7`|*Apotheosized*||″|
|`6`|*Zenith*||Astronomy|
|`8`|*Void Star*||David Szymanski's *Iron Lung*|
|`9`|*Substance*|Used along with a characteristic, notion or property related to the entity,<br>__*e.g.*__ *"Avery, Substance of Knowledge"*|Philosophy|
|`10`|*Essence*|Used along with a characteristic, notion or property related to the entity,<br>__*e.g.*__ *"Avery, Essence of Time"*|″|

&nbsp;

#### Necromancer

|Rank|Title|Remarks|Origin/Reference/Inspiration|
|:-:|:-:|:-|:-:|
|`0`|*Judge*|__Unused__ (automatically incremented).<br>Used for debugging purposes.|Occult tarot __(Judgement ⅩⅩ)__|
|`1`|*Dark Young*||H.P. Lovecraft's *Notebook Found in a Deserted House*|
|`2`|*Stygian Kraken*||≈ *Warhammer 40,000*|
|`3`|*Abysswalker*||*Dark Souls*|
|`4`|*Nemesis*||*Warhammer 40,000*|
|`5`|*Night Lord*||″|
|`6`|*Blood Angel*||″|
|`7`|*Gravelord*||*Dark Souls*|
|`8`|*Lord of Decay*||*Warhammer 40,000*|
|`9`|*Lord of Cinder*||*Dark Souls*|
|`10`|*Dark Sun*||″|

&nbsp;

#### Priest

|Rank|Title|Remarks|Origin/Reference/Inspiration|
|:-:|:-:|:-|:-:|
|`0`|*Judge*|__Unused__ (automatically incremented).<br>Used for debugging purposes.|Occult tarot __(Judgement ⅩⅩ)__|
|`1`|*Ruin Sentinel*||*Dark Souls Ⅱ*|
|`2`|*Sanctuary Guardian*||*Dark Souls*|
|`3`|*Knight*||≟ *Dark Souls Ⅱ*|
|`4`|*Crusader*||≟ *Warhammer 40,000*|
|`5`|*Royal Aegis*||*Dark Souls Ⅱ*|
|`6`|*War Bearer*||*Warhammer 40,000*|
|`7`|*Fallen Star*||″|
|`8`|*Reborn, The*|*__e.g.__ "Avery the Reborn"*|″|
|`9`|*Angel of Absolution*||″|
|`10`|*Templar of Eternity*||″|

<!--&nbsp;

#### Rogue

|Rank|Title|Remarks|Origin/Reference/Inspiration|
|:-:|:-:|:-|:-:|
|`0`|*Judge*|__Unused__ (automatically incremented).<br>Used for debugging purposes.|Occult tarot __(Judgement ⅩⅩ)__|
|`1`|*Major*||*Metal Gear Solid 2: Sons of Liberty*|
|`2`|*Colonel*||*Metal Gear Solid*|
|`3`|*Psycho Mantis*||″|
|`4`|*Gray Fox*||″|
|`5`|*Revolver Ocelot*||″|
|`6`|*Solidus Snake*||*Metal Gear Solid 2: Sons of Liberty*|
|`7`|*Liquid Snake*||*Metal Gear Solid*|
|`8`|*Solid Snake*||″|
|`9`|*Boss, The*|Overwrites the character's name<br>*__i.e.__* the character's name solely becomes *"The Boss"*|*Metal Gear Solid 3: Snake Eater*|
|`10`|*Big Boss*|Overwrites the previous title (*"The Boss"*) to *"Big Boss"*|″|-->

&nbsp;

#### Warrior

|Rank|Title|Remarks|Origin/Reference/Inspiration|
|:-:|:-:|:-|:-:|
|`0`|*Judge*|__Unused__ (automatically incremented).<br>Used for debugging purposes.|Occult tarot __(Judgement ⅩⅩ)__|
|`1`|*Settler*||*Sid Meier's Civilization Ⅵ*|
|`2`|*Chieftain*||″|
|`3`|*Warliege*||″|
|`4`|*Margrave*|Used along with a location name,<br>__*e.g.*__ *"Avery, Margrave of Anytown"*|″|
|`5`|*Monarch*|Used along with a location name,<br>__*e.g.*__ *"Avery, Monarch of Anytown"*|″|
|`6`|*Autocrat*|Used along with a location name,<br>__*e.g.*__ *"Avery, Autocrat of Anytown"*|″|
|`7`|*Immortal*||″|
|`8`|*Deity*||″|
|`9`|*Word Eater*||*Warhammer 40,000*|
|`10`|*Devourer of Gods*||*Dark Souls Ⅲ*|

---

## Traits

This section regards data related to the player character's different [attributes](https://en.wikipedia.org/wiki/Attribute_(role-playing_games)) and [statistics](https://en.wikipedia.org/wiki/Statistic_(role-playing_games)).

|Trait|Symbol|Description|Remarks|
|:-:|:-:|:-|:-|
|Constitution|`CON`|*"[...] character’s ability to resist [...] and to recover from damage received."* ([Angband Documentation](https://angband.readthedocs.io/en/latest/birth.html#stats)).<br>Proportional to the character's overall defense and recuperation.||
|Dexterity|`DEX`|*"[...] combination of __agility__ and quickness."* ([Angband Documentation](https://angband.readthedocs.io/en/latest/birth.html#stats)).<br>Proportional to the character's chances of hitting and dodging.||
|Intelligence|`INT`|*"[...] spellcasting abilities of spellcasters from the __arcane and shadow realms__"* ([Angband Documentation](https://angband.readthedocs.io/en/latest/birth.html#stats)).<br>Proportional to the number of spells per level and overall spellcasting success.||
|Speed|`SPD`|Player character's reflexes/attack speed.|Is only used to determine who strikes first in combat.|
|Strength|`STR`|Raw physical strength.<br>Proportional to the chances of hitting as well as said hit's overall damage.||
|Wisdom|`WIS`|*"[...] ability of a ___priest___ [...] to use prayers, [...] verses, just like intelligence __affects spellcasting__."* ([Angband Documentation](https://angband.readthedocs.io/en/latest/birth.html#stats)).<br>Proportional to the number of spells per level and overall spellcasting success.||

---

## *Subsistence gifts*

> It appears the gods have deemed you worthy of their omniscient heed; as such, they adjudged that your subsistence shall be graced with peculiarity.
> 
> From the depths of their creationistic will, they conjure a set of divine gifts. Whether these make you whole or bring you harm, they were wilfully made as they are, all according to unfathomable sacred plans.

This section regards the starting boons that the player can choose from uring character creation. These can bring the player up as much as they can bring them down.

&nbsp;

### __August herald__ ~ Deific wyrd | ↑`EXP` rate

> After much pondering, the gods have discerned something in you: not only is your existence bound to peculiarity, it is also bound to an eminence akin to that of a god, if not greater. You thus possess a divinely-crafted herald by your side since birth.

Increases the rate at which the player gains experience. Allows the player to level up faster in the long run.

Unlocks the possibility of being granted the random nickname *"the eminent"* (e.g. *"Avery the eminent"*).

&nbsp;

### __Bloodstained mark__ ~ Blood-spilt fortitude | (↑`CON`, ↑`STR`) & (↓`DEX`, ↓`SPD`)

> A unique mark on your skin and the shade of your wounds hint at the spilling of a ravaging beast's blood during your conception. Echoes of your unprecedented might reach far and wide.

Increases the character's strength (`STR`) and constitution (`CON`). On the contrary, decreases the character's dexterity (`DEX`) and speed (`SPD`).

Unlocks the possibility of being granted the random nickname *"the blood-bound"* (e.g. *"Avery the blood-bound"*).

&nbsp;

### __Lifelong breeze__ ~ Nimble limbs | ↑`SPD`

> From the lightest of clays you shall be modelled, and at your sides shall always blow an aiding waft, allowing for your limbs to require noticeably much lesser efforts to stir.

Increases the character's speed (`SPD`), increasing the chance to strike first in combat.

Unlocks the possibility of being granted the random nickname *"the hasty"* (e.g. *"Avery the hasty"*).

&nbsp;

### __*Suprēmum lexicon*__ ~ Innate scholarship | ↑`INT` & ↓`WIS`

> In your possession for as long as you can remember, this dictionary helps you translate works pertaining to magic written in languages ranging from across the world.

Increases the character's intelligence (`INT`) as well as the rate at which it augments with experience. On the contrary, decreases the character's wisdom (`WIS`), lowering the character's ability to perform White magic.

Unlocks the possibility of being granted the random nickname *"the prophetic"* (e.g. *"Avery the prophetic"*).

&nbsp;

### __Timeless candle__ ~ Sky-born oracle | ↑`WIS` & ↓`INT`

> Intrinsically linked to the aethyr via an undending candle's blaze, your wisdom transcends that of a common individual. As such, your magical prowesses appear to flourish even in the most sodden of quagmires.

Increases the character's wisdom (`WIS`) as well as the rate at which it augments with experience. On the contrary, decreases the character's intelligence (`INT`), lowering the character's ability to perform Arcane and Black magic.

Unlocks the possibility of being granted the random nickname *"the prophetic"* (e.g. *"Avery the prophetic"*).

---

## Status effects

This section regards the different effects that can modify the player character's status and overall state of being. They are usually determined by the consequences of an external cause (such as a physical injury, a hex or some other event that was _inevitable_.)

Inspired by the object flags in Angband:

![](/__prep/docs/assets/specs/playerStates.png)

&nbsp;

These states go as follows:

|State|Symbol|Description|Remarks|
|:-:|:-:|:-|:-|
|Acid-splattered|`ACID`|Describes the character having had acid/corrosive substance·s projected upon them, from which ensues a corrosion (whose strength and duration depend on certain factors).|__*aka*__ *Corroded*;<br>was named this way for clarity's sake.|
|Ablaze|`BLAZ`|Describes the character currently burning after being set on fire, either by an external cause or seemingly spontaneous combustion.|__*aka*__ *On fire*, *Aflame*;<br>was named this way to the deliberate detriment of clarity due to its __cool-sounding properties__.|
|Blessed|`BLES`|Describes the character receiving or having temporarily received a deity/celestial being's benediction·s.||
|Blind|`BLND`|Describes the character being prone to partial or permanent cecity.|Depending on the cecity's severity and origin (a wound, a spell...), will lasts for a variable amount of time (a few turns, forever...) and most importantly __will impair the player's vision of the map__ (limitation to a short range around the character, everything aside from the character itself...).<br>Can be counteracted by various means such as magic.|
|Frozen|`FROZ`|Describes the character immobilized from cold, either from environmental causes or "more commonly" from magic.|Depending on the severity and origin of the freezing, hinders more or less gravely the character's movement, for a certain amount of turns.|
|Hexed|`HEXD`|~~Describes the character having encountered [Hex Maniacs](https://bulbapedia.bulbagarden.net/wiki/Hex_Maniac_(Trainer_class))~~<br>Describes the character being prone to/under the influence of a curse of some type.|Due to the varied nature of curses throughout *Arithmancy*, these can have very diverse and sometimes completely unpredicatable effects on the player's character.|
|Poisoned|`POIS`|Describes the character being harmed in some way by (a) poisonous substance·s.|Although generally of __physical__ nature, the poisoning can also target the character's __mana__ (which will have no consequences if the former has none) or other character traits.<br>Of course, the poisoning's duration and severity depend on several factors, such as its origin, nature...|