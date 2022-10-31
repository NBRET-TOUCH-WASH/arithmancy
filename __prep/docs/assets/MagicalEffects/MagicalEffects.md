# ![now with real layers inside!](/__prep/docs/assets/cromniomancy.png)

In this document, the terms *"player"* and *"[player] character"* are used interchangeably.

## Magical effects

#### `0083` : *After each spell, caster is afraid of his own name*

Implementation:<br>
For a certain amount of turns after casting a spell, everytime the player looks at their stats (and thus their name appears), their character gets more afraid, up until they can't take it anymore and die of fear

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

&nbsp;

#### `1767` : *Caster think that their face is just a mask they wear on their skull*

Implementation:<br>
Upon realizing that their face is but a mask they are currently wearing, the player character starts furiously trying to remove said mask, and ends up tearing their face off, dying from blood loss.

Derivatives:<br>
- The player's character come to their senses before dying; depending on the severity of their wound, their state ranges from unharmed to passing out from shock and blood loss.
    - With this derivative, the "narrator" expresses how *"It's no use!"* and gets the player to come to their senses.

&nbsp;

#### `1999` : *"Caster's face is a mask"*

Implementation:<br>
Upon actually realizing that their face legitimately is nothing but a mask they are currently wearing, they gently take their face out of its slot to examine it; when doing so, in shock, they let it fall to the ground. This, in turn, makes movement from the player impossible, as the rest of their body (which consequently is blind) stumble about in order to find their face again. This triggers a Game Over (Death scenario)