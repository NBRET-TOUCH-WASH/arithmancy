# ![more layers](/__prep/docs/assets/cromniomancy.png)

Git planning for the __production phase__ of *Arithmancy*.

&nbsp;

Unless specified otherwise, all date intervals are to be understood as ![a;b](/__prep/docs/assets/timeIntervals.png) [segments](https://en.wikipedia.org/wiki/Interval_(mathematics)#Note_on_conflicting_terminology).

An issue in *mermaid-js*' GitGraph rendering makes the completion of the production phase Git graph impossible at the time of writing. As such, it is currently incomplete as well as being buggy is left "as is".

&nbsp;

### Contents
- [Documentation branch](#documentation-branch)
    - [Devlogs](#devlogs)
- [Source branch](#source-branch)
- [Main menu](#main-menu)
- [Character creation](#character-creation)
- [Maps](#maps)
- [Entities](#entities)

---

## Documentation branch

&nbsp;

### Devlogs

---

## Source branch

---

## Main menu

---

## Character creation

---

## Maps

---

## Entities

---

## Postamble

The production phase for *Arithmancy* should last for __30 days__ of the game's __≈47 days (1 month and 17 days)__ of allowed development (basically ranging from the __1st of November 2022__ (`2022-11-01`) to the __30th of November 2022__ (`2022-11-30`) ) reaching the project's deadline.

From this will arise version `v1.0.0`, after which the game will quite possibly enter its __post-mortem phase__ - i.e. additional development independant of the original project - without any hiccups.

```mermaid
%%{init: { 'logLevel': 'debug', 'theme': 'base', 'gitGraph': {'rotateCommitLabel': true}} }%%
gitGraph

checkout main
commit id:"Intitial release" tag: "v0.0.0"

branch prod-docs
commit id:"Docs setup"
branch prod-devlogs

checkout main
branch prod-src
commit id:"Prod setup"

branch prod-main-menu
commit id:"Main menu"
checkout prod-src
merge prod-main-menu

checkout prod-devlogs
commit id:"Devlog #1 : Main menu"
checkout prod-docs
merge prod-devlogs
commit id:"Main menu docs"


checkout prod-src
branch prod-character-creation
commit id:"Biography"
commit id:"Fantasy race"
commit id:"Class"
commit id:"Traits"
commit id:"Subsistence gifts"
checkout prod-src
merge prod-character-creation

checkout prod-devlogs
commit id:"Devlog #2 : Main menu"
checkout prod-docs
merge prod-devlogs
commit id:"Character creation docs"


checkout prod-src
branch prod-maps
commit id:"Static maps"
commit id:"Dynamic elements"
commit id:"Maps matrix"
checkout prod-src
merge prod-maps

checkout prod-devlogs
commit id:"Devlog #3 : Maps"
checkout prod-docs
merge prod-devlogs
commit id:"Maps docs"


checkout prod-src
branch prod-entities
commit id:"Player entity"
checkout prod-src
merge prod-entities

checkout prod-devlogs
commit id:"Devlog #4 : Player entity"
checkout prod-docs
merge prod-devlogs
commit id:"Player entity docs"


checkout main
merge prod-src tag:"v0.1.0"
merge prod-docs

checkout prod-entities
commit id:"Creatures" type:HIGHLIGHT
checkout prod-src
merge prod-entities

checkout prod-devlogs
commit id:"Devlog #5 : Creatures"
checkout prod-docs
merge prod-devlogs
commit id:"Creatures docs"


checkout main
merge prod-src tag:"v0.2.0"
merge prod-docs


checkout prod-src
branch prod-ui
commit id:"Main panel"
commit id:"Player stats panel"
commit id:"Logs panel"
commit id:"Entity interactions panel"
commit id:"Items panels"
checkout prod-src
merge prod-ui

checkout prod-src
branch prod-interactions
commit id:"Entities interactions"
commit id:"Items interactions"
checkout prod-src
merge prod-interactions
```
<!--
checkout prod-src
branch prod-combat
commit id:"Combat" type:HIGHLIGHT
checkout prod-src
merge prod-combat-->