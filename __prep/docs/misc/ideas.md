# NSI RPG project ideas

### Contents
- [Info](#info)
    - [Title](#title)
- [Gameplay](#gameplay)
    - [Character Creation](#character-creation)
    - [Combat](#combat)
    - [Player actions](#player-actions)
    - [UI](#ui)
    - [Easter eggs](#easter-eggs)

---

## Info

### Title

- [x] *Arithmancy*
    - > "assigning numerical value to a word or phrase" - [Wikipedia](https://en.wikipedia.org/wiki/Methods_of_divination#A)
- [ ] *Favomancy*
- [ ] *Cromniomancy*
    - Because that's funny as fuck

---

## Gameplay

### Character creation

A __gender selection__ functionality:<br>
A player has the ability to select their gender during character creation, either from a premade list *(1)* or by manual input (useful for "rare" genders), e.g. :<br>
> `Select a gender:`<br>
> `¤ Enby ¤ Female ¤ Male`<br>
> 
> __[MANUAL SELECTION]__<br>
> `[√] Other`<br>
> `Input a gender: >▮`

&nbsp;

A __random character adjective__:<br>
A random adjective is assigned to the player at "birth", making for replayability value, as to bring changes with each game, e.g. :<br>
> Billï the *adventurous* Warrior

> Godrick the *courteous* Warrior

> Bob Bingi the *cooperative* Mage

> Salazar the *dutiful* Mage

... or:

> `Player stats:`<br>
> `Camilia, LVL2 Warrior (respectful)`

> `Player stats:`<br>
> `Avery, LVL7 Mage (bashful)`

&nbsp;

### Combat

A __sigil obtention__ system:<br>
Slaying enemies in combat allows for the player to obtain - aside from XP and items - [sigils](https://en.wikipedia.org/wiki/Sigil), which can then be used in other parts of the game.<br>
__*cf. Divination system*__

&nbsp;

### Player actions

A **divination system**:<br>
[As in Dwarf Fortress](https://dwarffortresswiki.org/index.php/DF2014:Die#Adventurer_Mode), the player can use items to perform divination. It could hold some rare but interesting (or just plain [funny](/__prep/docs/assets/NLRMEv2.pdf)) effects and alternatively, be completely useless.<br>
Unlike in Drawf Fortress, however, divination could be performed with more items than a simple die, using the [numerous divination techniques found throughout the world and its History](https://en.wikipedia.org/wiki/Methods_of_divination), e.g. :<br>
> __Cromniomancy__<br>
> `Use the onions for what?` ▶ `Perform cromniomancy`<br>
> You carve a sigil in the onions... They now seem to reveal a terrible fate!

> __Cyclicomancy__<br>
> `Do what with the chalice?` ▶ `Drink content`<br>
> You drink the chalice's content... You feel as if your destiny was becoming clearer by the second.

> __Favomancy__<br>
> `Use the beans for what?` ▶ `Perform favomancy`<br>
> You throw the beans on the ground. They land in a star-shaped pattern! This does not bode well...

&nbsp;

### UI

A __random enemy adjective__:<br>
Every enemy encountered has an adjective next to their name in order to add variety, e.g. :<br>
> You encounter a *[adjective]* *[enemy]*!

Possible adjectives include: *"creepy"*, *"bulbous"*, *"dreadful"*, *"disgusting"*...

__And why not make it so that a certain adjective adds a certain peculiarity said enemy?__

&nbsp;

An __textual attribute "plurality"__ functionality:<br>
Words (e.g. the `smell` attribute from the `IFecalFunny` interface) are stored as a dictionary that holds several forms of a same word, used according to the context of the sentence, e.g. :<br>
> __[ADJECTIVE DICT]__ `{"noun":"rot", "adjective":"rotten"}`<br>
> __[ENCOUNTER TEXT]__ You encounter a *rotten* skeleton!<br>
> __[EXAMINATION TEXT]__ You take a close look at the Spoopy skeleton... they smell like *rot*!

&nbsp;

### Easter eggs

Each skeleton enemy has a very low probability of __being named "Mr. Bones"__, "Mr. Skeltal" or something of the such