# ![layerzzzzz](/__prep/docs/assets/cromniomancy.png)

Specifications for the __graphics__ in *Arithmancy*.

At the time of writing, colors from preparatory images/sketches are __not__ to be taken into account.

### Contents
- [Global specifications](#global-specifications)
    <!-- - [Resolution](#resolution)-->
    - [Colors](#colors)
    <!-- - [Character set](#character-set)-->
- [Main menu](#main-menu)
- [Main game](#main-game)
- [Game Over screen](#game-over-screen)

---

## Global specifications

This section focuses on graphics settings that apply to every aspect of the game.
<!--
&nbsp;

### Resolution

The game's resolution is not specified in pixels (`px`), rather, it is specified in *COLUMNS* and *LINES*, manipulated according to a ![coordinates](/__prep/docs/assets/graphics/coordinates.png) coordinate system.

- Resolution (*COLUMNS*x*LINES*): `115x65`
    - Width (*COLUMNS*) : `115`
    - height (*LINES*): `65`-->

&nbsp;

### Colors

For ease of usage, user experience and aesthetic value, *Arithmancy* uses a set of predefined colors ~~totally not taken from [*Dwarf Fortress*](https://dwarffortresswiki.org/index.php/DF2014:Color#Color_tokens)~~:

#### *Blue* (`BLUE`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|Dark Blue|`DARK_BLUE`|`0,0,139`|`#00008B`|![darkBlue](/__prep/docs/assets/graphics/colors/blue/darkBlue.png)|
|*Cobalt*|`COBALT`|`0,71,171`|`#0047AB`|![cobalt](/__prep/docs/assets/graphics/colors/blue/cobalt.png)|
|*Slate* Gray|`SLATE_GRAY`|`112,128,144`|`#708090`|![slateGray](/__prep/docs/assets/graphics/colors/blue/slateGray.png)|

#### *Light Blue* (`LBLUE`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|Blue|`BLUE`|`0,0,255`|`#0000FF`|![blue](/__prep/docs/assets/graphics/colors/lightBlue/blue.png)|
|*Azure*|`AZURE`|`0,127,255`|`#007FFF`|![azure](/__prep/docs/assets/graphics/colors/lightBlue/azure.png)|
|*Periwinkle*|`PERIWINKLE`|`204,204,255`|`#CCCCFF`|![periwinkle](/__prep/docs/assets/graphics/colors/lightBlue/periwinkle.png)|

#### *Brown* (`BROWN`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Fern* Green|`FERN_GREEN`|`79,121,66`|`#4F7942`|![fernGreen](/__prep/docs/assets/graphics/colors/brown/fernGreen.png)|
|Dark *Olive*|`DARK_OLIVE`|`85,104,50`|`#556832`|![darkOlive](/__prep/docs/assets/graphics/colors/brown/darkOlive.png)|
|Dark Brown|`DARK_BROWN`|`101,67,33`|`#654321`|![darkBrown](/__prep/docs/assets/graphics/colors/brown/darkBrown.png)|
|*Taupe Medium*|`TAUPE_MEDIUM`|`103,76,71`|`#674C47`|![taupeMedium](/__prep/docs/assets/graphics/colors/brown/taupeMedium.png)|
|*Auburn*|`AUBURN`|`111,53,26`|`#6F351A`|![auburn](/__prep/docs/assets/graphics/colors/brown/auburn.png)|
|*Sepia*|`SEPIA`|`112,66,20`|`#704214`|![sepia](/__prep/docs/assets/graphics/colors/brown/sepia.png)|
|*Raw Umber*|`RAW_UMBER`|`115,74,18`|`#734A12`|![rawUmber](/__prep/docs/assets/graphics/colors/brown/rawUmber.png)|
|*Russet*|`RUSSET`|`117,90,87`|`#755A57`|![russet](/__prep/docs/assets/graphics/colors/brown/russet.png)|
|*Cinnamon*|`CINNAMON`|`123,63,0`|`#7B3F00`|![cinnamon](/__prep/docs/assets/graphics/colors/brown/cinnamon.png)|
|*Olive*|`OLIVE`|`128,128,0`|`#808000`|![olive](/__prep/docs/assets/graphics/colors/brown/olive.png)|
|*Burnt Umber*|`BURNT_UMBER`|`138,51,36`|`#8A3324`|![burntUmber](/__prep/docs/assets/graphics/colors/brown/burntUmber.png)|
|Brown|`BROWN`|`150,75,0`|`#964B00`|![brown](/__prep/docs/assets/graphics/colors/brown/brown.png)|
|*Brass*|`BRASS`|`181,166,66`|`#B5A642`|![brass](/__prep/docs/assets/graphics/colors/brown/brass.png)|
|*Taupe Pale*|`TAUPE_PALE`|`188,152,126`|`#BC987E`|![taupePale](/__prep/docs/assets/graphics/colors/brown/taupePale.png)|

#### *Cyan* (`CYAN`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Midnight* Blue|`MIDNIGHT_BLUE`|`0,51,102`|`#003366`|![midnightBlue](/__prep/docs/assets/graphics/colors/cyan/midnightBlue.png)|
|*cerulean*|`CERULEAN`|`0,123,167`|`#007BA7`|![cerulean](/__prep/docs/assets/graphics/colors/cyan/cerulean.png)|
|*Teal*|`TEAL`|`0,128,128`|`#008080`|![teal](/__prep/docs/assets/graphics/colors/cyan/teal.png)|
|*Pine* Green|`PINE_GREEN`|`1,121,111`|`#01796F`|![pineGreen](/__prep/docs/assets/graphics/colors/cyan/pineGreen.png)|
|*Sea* Green|`SEA_GREEN`|`46,139,87`|`#2E8B57`|![seaGreen](/__prep/docs/assets/graphics/colors/cyan/seaGreen.png)|

#### *Light Cyan* (`LCYAN`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Aqua*|`AQUA`|`0,255,255`|`#00FFFF`|![aqua](/__prep/docs/assets/graphics/colors/lightCyan/aqua.png)|
|*Turquoise*|`TURQUOISE`|`48,213,200`|`#30D5C8`|![turquoise](/__prep/docs/assets/graphics/colors/lightCyan/turquoise.png)|
|*Aquamarine*|`AQUAMARINE`|`127,255,212`|`#7FFFD4`|![aquamarine](/__prep/docs/assets/graphics/colors/lightCyan/aquamarine.png)|
|*Sky* Blue|`SKY_BLUE`|`135,206,235`|`#87CEEB`|![skyBlue](/__prep/docs/assets/graphics/colors/lightCyan/skyBlue.png)|
|*Mint* Green|`MINT_GREEN`|`152,255,152`|`#98FF98`|![mintGreen](/__prep/docs/assets/graphics/colors/lightCyan/mintGreen.png)|
|Light Blue|`LIGHT_BLUE`|`173,216,230`|`#ADD8E6`|![lightBlue](/__prep/docs/assets/graphics/colors/lightCyan/lightBlue.png)|
|*Moss* Green|`MOSS_GREEN`|`173,223,173`|`#ADDFAD`|![mossGreen](/__prep/docs/assets/graphics/colors/lightCyan/mossGreen.png)|
|*Pale* Blue|`PALE_BLUE`|`175,238,238`|`#AFEEEE`|![paleBlue](/__prep/docs/assets/graphics/colors/lightCyan/paleBlue.png)|

#### *Dark Gray* (`DGRAY`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|Black|`BLACK`|`0,0,0`|`#000000`|![black](/__prep/docs/assets/graphics/colors/darkGray/black.png)|
|*Charcoal*|`CHARCOAL`|`54,69,79`|`#36454F`|![charcoal](/__prep/docs/assets/graphics/colors/darkGray/charcoal.png)|
|*Taupe*|`TAUPE`|`72,60,50`|`#483C32`|![taupe](/__prep/docs/assets/graphics/colors/darkGray/taupe.png)|
|*Taupe* purple|`TAUPE_PURPLE`|`80,64,77`|`#50404D`|![taupePurple](/__prep/docs/assets/graphics/colors/darkGray/taupePurple.png)|
|Gray|`GRAY`|`128,128,128`|`#808080`|![gray](/__prep/docs/assets/graphics/colors/darkGray/gray.png)|
|*Taupe* gray|`TAUPE_GRAY`|`139,133,137`|`#8B8589`|![taupeGray](/__prep/docs/assets/graphics/colors/darkGray/taupeGray.png)|

#### *Light Gray* (`LGRAY`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Ash*|`ASH`|`178,190,181`|`#B2BEB5`|![ash](/__prep/docs/assets/graphics/colors/lightGray/ash.png)|
|*Silver*|`SILVER`|`192,192,192`|`#C0C0C0`|![silver](/__prep/docs/assets/graphics/colors/lightGray/silver.png)|

#### *Green* (`GREEN`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Jade*|`JADE`|`0,168,107`|`#00A86B`|![jade](/__prep/docs/assets/graphics/colors/green/jade.png)|
|Dark Green|`DARK_GREEN`|`1,50,32`|`#013220`|![darkGreen](/__prep/docs/assets/graphics/colors/green/darkGreen.png)|

#### *Light Green* (`LGREEN`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|Green|`GREEN`|`0,255,0`|`#00FF00`|![Green Hill Zone](/__prep/docs/assets/graphics/colors/lightGreen/green.png)|
|*Spring* Green|`SPRING_GREEN`|`0,255,127`|`#00FF7F`|![springGreen](/__prep/docs/assets/graphics/colors/lightGreen/springGreen.png)|
|Emerald|`EMERALD`|`80,200,120`|`#50C878`|![emerald](/__prep/docs/assets/graphics/colors/lightGreen/emerald.png)|
|*Chartreuse*|`CHARTREUSE`|`127,255,0`|`#7BFF00`|![chartreuse](/__prep/docs/assets/graphics/colors/lightGreen/chartreuse.png)|

#### *Magenta* (`MAGENTA`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|Dark *Indigo*|`DARK_INDIGO`|`49,0,98`|`#310062`|![darkIndigo](/__prep/docs/assets/graphics/colors/magenta/darkIndigo.png)|
|Dark *Violet*|`DARK_VIOLET`|`66,49,137`|`#423189`|![darkViolet](/__prep/docs/assets/graphics/colors/magenta/darkViolet.png)|
|*Indigo*|`INDIGO`|`75,0,138`|`#4B0082`|![indigo](/__prep/docs/assets/graphics/colors/magenta/indigo.png)|
|*Eggplant*|`EGGPLANT`|`97,64,81`|`#614051`|![eggplant](/__prep/docs/assets/graphics/colors/magenta/eggplant.png)|
|Plum|`PLUM`|`102,0,102`|`#660066`|![plum](/__prep/docs/assets/graphics/colors/magenta/plum.png)|
|Purple|`PURPLE`|`102,0,153`|`#660099`|![purple](/__prep/docs/assets/graphics/colors/magenta/purple.png)|

#### *Light Magenta* (`LMAGENTA`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Violet*|`VIOLET`|`139,0,255`|`#8B00FF`|![violet](/__prep/docs/assets/graphics/colors/lightMagenta/violet.png)|
|*Amethyst*|`AMETHYST`|`153,102,204`|`#9966CC`|![darkIndigo](/__prep/docs/assets/graphics/colors/lightMagenta/amethyst.png)|
|*Lilac*|`LILAC`|`200,162,200`|`#C8A2C8`|![lilac](/__prep/docs/assets/graphics/colors/lightMagenta/lilac.png)|
|*Puce*|`PUCE`|`204,136,153`|`#CC8899`|![puce](/__prep/docs/assets/graphics/colors/lightMagenta/puce.png)|
|*Pale* Chestnut|`PALE_CHESTNUT`|`221,172,175`|`#DDADAF`|![paleChestnut](/__prep/docs/assets/graphics/colors/lightMagenta/paleChestnut.png)|
|*Heliotrope*|`HELIOTROPE`|`223,115,255`|`#DF73FF`|![heliotrope](/__prep/docs/assets/graphics/colors/lightMagenta/heliotrope.png)|
|*Fuschia*|`FUSCHIA`|`244,0,161`|`#F400A1`|![fuschia](/__prep/docs/assets/graphics/colors/lightMagenta/fuschia.png)|
|*Pale* Pink|`PALE_PINK`|`250,218,221`|`#FADADD`|![palePink](/__prep/docs/assets/graphics/colors/lightMagenta/palePink.png)|
|Pink|`PINK`|`255,192,203`|`#FFC0CB`|![pink](/__prep/docs/assets/graphics/colors/lightMagenta/pink.png)|

#### *Red* (`RED`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|Dark *Scarlet*|`DARK_SCARLET`|`86,3,25`|`#560319`|![darkScarlet](/__prep/docs/assets/graphics/colors/red/darkScarlet.png)|
|*Maroon*|`MAROON`|`128,0,0`|`#800000`|![maroon](/__prep/docs/assets/graphics/colors/red/maroon.png)|
|*Taupe* rose|`TAUPE_ROSE`|`144,93,93`|`#905D5D`|![taupeRose](/__prep/docs/assets/graphics/colors/red/taupeRose.png)|
|*Mauve Taupe*|`MAUVE_TAUPE`|`145,95,109`|`#915F6D`|![mauveTaupe](/__prep/docs/assets/graphics/colors/red/mauveTaupe.png)|
|Dark *Tan*|`DARK_TAN`|`145,129,81`|`#918151`|![darkTan](/__prep/docs/assets/graphics/colors/red/darkTan.png)|
|*Carmine*|`CARMINE`|`150,0,24`|`#960018`|![carmine](/__prep/docs/assets/graphics/colors/red/carmine.png)|
|*Taupe Sandy*|`TAUPE_SANDY`|`150,113,23`|`#967117`|![taupeSandy](/__prep/docs/assets/graphics/colors/red/taupeSandy.png)|
|Dark *Chestnut*|`DARK_CHESTNUT`|`152,105,96`|`#986960`|![darkChestnut](/__prep/docs/assets/graphics/colors/red/darkChestnut.png)|
|Pale Brown|`PALE_BROWN`|`152,118,84`|`#987654`|![paleBrown](/__prep/docs/assets/graphics/colors/red/paleBrown.png)|
|*Mauve*|`MAUVE`|`153,51,102`|`#993366`|![mauve](/__prep/docs/assets/graphics/colors/red/mauve.png)|
|Red Purple|`RED_PURPLE`|`178,0,75`|`#B2004B`|![redPurple](/__prep/docs/assets/graphics/colors/red/redPurple.png)|
|*Rust*|`RUST`|`183,65,14`|`#B7410E`|![rust](/__prep/docs/assets/graphics/colors/red/rust.png)|
|*Copper*|`COPPER`|`184,115,51`|`#B87333`|![copper](/__prep/docs/assets/graphics/colors/red/copper.png)|

#### *Light Red* (`LRED`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Mahogany*|`MAHOGANY`|`192,64,0`|`#C04000`|![mahogany](/__prep/docs/assets/graphics/colors/lightRed/mahogany.png)|
|*Cardinal*|`CARDINAL`|`196,30,58`|`#C41E3A`|![cardinal](/__prep/docs/assets/graphics/colors/lightRed/cardinal.png)|
|*Ochre*|`OCHRE`|`204,119,34`|`#CC7722`|![ochre](/__prep/docs/assets/graphics/colors/lightRed/ochre.png)|
|*Chestnut*|`CHESTNUT`|`205,92,92`|`#CD5C5C`|![chestnut](/__prep/docs/assets/graphics/colors/lightRed/chestnut.png)|
|*Bronze*|`BRONZE`|`205,127,50`|`#CD7F32`|![bronze](/__prep/docs/assets/graphics/colors/lightRed/bronze.png)|
|Light Brown|`LIGHT_BROWN`|`205,133,63`|`#CD853F`|![lightBrown](/__prep/docs/assets/graphics/colors/lightRed/lightBrown.png)|
|*Crimson*|`CRIMSON`|`220,20,60`|`#DC143C`|![『Kingu Kurimuzon』](/__prep/docs/assets/graphics/colors/lightRed/crimson.png)|
|*Chocolate*|`CHOCOLATE`|`210,105,30`|`#DC691E`|![chocolate](/__prep/docs/assets/graphics/colors/lightRed/chocolate.png)|
|*Vermilion*|`VERMILION`|`227,66,52`|`#E34234`|![vermilion](/__prep/docs/assets/graphics/colors/lightRed/vermilion.png)|
|Dark Pink|`DARK_PINK`|`231,84,128`|`#E75480`|![darkPink](/__prep/docs/assets/graphics/colors/lightRed/darkPink.png)|
|*Burnt Sienna*|`BURNT_SIENNA`|`233,116,81`|`#E97451`|![burntSienna](/__prep/docs/assets/graphics/colors/lightRed/burntSienna.png)|
|*Rose*|`ROSE`|`244,194,194`|`#F4C2C2`|![rose](/__prep/docs/assets/graphics/colors/lightRed/rose.png)|
|Red|`RED`|`255,0,0`|`#FF0000`|![red](/__prep/docs/assets/graphics/colors/lightRed/red.png)|
|*Scarlet*|`SCARLET`|`255,36,0`|`#FF2400`|![scarlet](/__prep/docs/assets/graphics/colors/lightRed/scarlet.png)|
|*Pumpkin*|`PUMPKIN`|`255,117,24`|`#FF7518`|![pumpkin](/__prep/docs/assets/graphics/colors/lightRed/pumpkin.png)|

#### *Yellow* (`YELLOW`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|Yellow Green|`YELLOW_GREEN`|`154,205,50`|`#9ACD32`|![yellowGreen](/__prep/docs/assets/graphics/colors/yellow/yellowGreen.png)|
|Green Yellow|`GREEN_YELLOW`|`173,255,47`|`#ADFF2F`|![greenYellow](/__prep/docs/assets/graphics/colors/yellow/greenYellow.png)|
|*Ecru*|`ECRU`|`194,178,128`|`#C2B280`|![ecru](/__prep/docs/assets/graphics/colors/yellow/ecru.png)|
|*Lime*|`LIME`|`204,255,0`|`#CCFF00`|![lime](/__prep/docs/assets/graphics/colors/yellow/lime.png)|
|*Tan*|`TAN`|`210,180,140`|`#D2B48C`|![tan](/__prep/docs/assets/graphics/colors/yellow/tan.png)|
|*Gold*|`GOLD`|`212,175,55`|`#D4AF37`|![gold](/__prep/docs/assets/graphics/colors/yellow/gold.png)|
|*Goldenrod*|`GOLDENROD`|`218,165,32`|`#DAA520`|![goldernrod](/__prep/docs/assets/graphics/colors/yellow/goldenrod.png)|
|*Flax*|`FLAX`|`238,220,130`|`#EEDC82`|![flax](/__prep/docs/assets/graphics/colors/yellow/flax.png)|
|*Pearl*|`PEARL`|`240,234,214`|`#F0EBD6`|![pearl](/__prep/docs/assets/graphics/colors/yellow/pearl.png)|
|*Buff*|`BUFF`|`240,220,130`|`#F0DC82`|![buff](/__prep/docs/assets/graphics/colors/yellow/buff.png)|
|*Saffron*|`SAFFRON`|`244,196,48`|`#F4C430`|![saffron](/__prep/docs/assets/graphics/colors/yellow/saffron.png)|
|*Lemon*|`LEMON`|`253,233,16`|`#FDE910`|![lemon](/__prep/docs/assets/graphics/colors/yellow/lemon.png)|
|Orange|`ORANGE`|`255,165,0`|`#FFA500`|![orange](/__prep/docs/assets/graphics/colors/yellow/orange.png)|
|*Amber*|`AMBER`|`255,191,0`|`#FFBF00`|![amber](/__prep/docs/assets/graphics/colors/yellow/amber.png)|
|Dark *Peach*|`DARK_PEACH`|`255,218,185`|`#FFDAB8`|![darkPeach](/__prep/docs/assets/graphics/colors/yellow/darkPeach.png)|
|*Golden* Yellow|`GOLDEN_YELLOW`|`255,223,0`|`#FFDF00`|![goldenYellow](/__prep/docs/assets/graphics/colors/yellow/goldenYellow.png)|
|*Peach*|`PEACH`|`255,229,180`|`#FFE5B4`|![peach](/__prep/docs/assets/graphics/colors/yellow/peach.png)|
|*Cream*|`CREAM`|`255,253,208`|`#FFFDD0`|![cream](/__prep/docs/assets/graphics/colors/yellow/cream.png)|
|Yellow|`YELLOW`|`255,255,0`|`#FFFF00`|![yellow](/__prep/docs/assets/graphics/colors/yellow/yellow.png)|

#### *White* (`WHITE`) colors:
|Name|Token|RGB|Hex|Sample|
|:-|:-|:-:|:-:|:-:|
|*Lavender*|`LAVENDER`|`255,255,240`|`#E6E6FA`|![lavender](/__prep/docs/assets/graphics/colors/white/lavender.png)|
|*Beige*|`BEIGE`|`245,245,220`|`#F5F5DC`|![beige](/__prep/docs/assets/graphics/colors/white/beige.png)|
|*Lavender blush*|`LAVENDER_BLUSH`|`255,240,245`|`#FFF0F5`|![lavenderBlush](/__prep/docs/assets/graphics/colors/white/lavenderBlush.png)|
|*Ivory*|`IVORY`|`255,255,240`|`#FFFFF0`|![ivory](/__prep/docs/assets/graphics/colors/white/ivory.png)|
|White|`WHITE`|`255,255,255`|`#FFFFFF`|![white](/__prep/docs/assets/graphics/colors/white/white.png)|

<!--
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
|*White*|`#ffffff`|`(255,255,0)`|*Yellow*|`#ffff00`|`(255,255,0)`|-->
<!--
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
|`♠`|Bush||-->

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