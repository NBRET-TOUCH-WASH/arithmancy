# ![now with real layers inside!](/__prep/docs/assets/cromniomancy.png)

In this document, the terms *"player"* and *"[player] character"* are used interchangeably.

## Magical effects

#### `0083` : *After each spell, caster is afraid of his own name*

Implementation:<br>
For a certain amount of turns, everytime the player looks at their stats (and thus their name appears), their character gets more afraid, up until they can't take it anymore and die of fear

&nbsp;

#### `0324` : *Before each spell, caster must say "The prophecy is fulfilled."*

Implementation:<br>
For a certain amount of turns, the player automatically says

> *"The prophecy is true."*

before casting a spell.

&nbsp;

#### `0327` : *Before each spell, caster must shout a different prime number*

Implementation:<br>
For a certain amount of turns, before casting a spell, the game automatically calculates a random prime number and gives it to say by the character.

&nbsp;

#### `0744` : *Caster disgorges 1d100 gold pieces*

Implementation:<br>
For one turn, the player spits out `1d100` gold pieces. Above a certain treshold of pieces, spitting said pieces out actually hurts the player and makes them lose a small amount of HP.

Derivatives:<br>
- The player undergoes the same effect but is spitting uranium ingots instead.