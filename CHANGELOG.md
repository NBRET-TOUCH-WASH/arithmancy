# Changelog
All notable changes to this project ~~will~~ *should* be documented in this file.

This file's format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and loosely adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It also uses [*The Beginner's Guide* level names](https://the-beginners-guide.fandom.com/wiki/List_of_levels) for it's versions codenames, as well as quotes from the levels' narration as a quote.

---

<!--!final version: ## [`v?.?.?`] - *"Exiting"*
> There's a bigger picture that all of their games are meant to play a role in.

----->


<!--!## [`v1.0.0`] - *"Entering"*
> The meaning of this game won't be clear just yet, please be patient with me [...] and I promise you'll see what makes it interesting.
---
-->

<!--? hopefully i find some use for this one, it's a special chapter of the game to me
## [`v?.?.?`] - *"Escape"*
> Okay this one is tough, it's going to kind of just spin its own wheels for a few minutes, hang with it.

---
-->

<!--? for some dungeon crawling aspect, some progression with the story?
## [`v?.?.?`] - *"Down"*
> And so we make one last descent, down to the final floor of the level.

---
-->

<!--? for interactions of some kind?
## [`v?.?.?`] - *"Whisper"*
> What's clear is that after making this something lodges itself in their brain, they want to do more of these really weird and experimental designs.

---
-->

<!--? for the implementation of the third axis in the maps matrix
## [`v?.?.?`] - *"Stairs"*
> It can be a very slow climb to get there.

---
-->

<!--? for item interaction, books reading, maybe?
## [`v?.?.?`] - *"Lecture"*
> This one gets a bit goofy.

---
-->

<!-- ! change "unreleased" to "pre-release" -->
## [`v0.1.0`] - *"Backwards"* | __(Pending release)__
> It works, because it gets out quick.

---


## [`v0.0.0`] - *"Intro"* | __(Pre-release)__
> Hi there. Thank you very much for playing *Arithmancy*.

&nbsp;

Undocumented changes are unsignificant as they do not correspond to the new structure.

### Added

- Transferred preliminary setup ([`530affb`](https://github.com/NBRET-TOUCH-WASH/arithmancy/commit/530affb))
- Project details
    - [README file](/README.md)
    - [License file](/LICENSE)
    - [Changelog](/CHANGELOG.md)
- Documentation
    - Documentation Asset·s
        - Possible reference material
            - [*The Net Libram of Random Magical Effects*](/__prep/docs/assets/NLRMEv2.pdf)
            - [`MagicalEffects.md`](__prep\docs\assets\MagicalEffects\MagicalEffects.md)
        - Game logo and associated files ([`cromniomancy.png`](/__prep/docs/assets/cromniomancy.png))
    - Miscellaneous
        - Semi-organized ideas list ([`ideas.md`](/__prep/docs/misc/ideas.md))
    - Specifications
        - Data
            - [Player data](__prep\docs\specs\data\playerData.md)
        - [Git planning](/__prep/docs/specs/git/)
            - [Preparatory phase](__prep\docs\specs\git\preparatoryPhaseGitPlanning.md)
            - [Production phase](__prep\docs\specs\git\productionPhaseGitPlanning.md)
        - Graphics ([`graphicsSpecs.md`](__prep\docs\specs\graphics\graphicsSpecs.md))
- Preparatory source
    - Asset·s ([`tilesheet160x160.png`](/__prep/src/tests/assets/tilesheet160x160.png))
    - [`tcod` tutorial](https://rogueliketutorials.com/tutorials/tcod/v2/)
    - Testing
        - [Graphics](__prep/src/tests/graphics)
            - Colors
            - Options list
            - Panels
            - Window