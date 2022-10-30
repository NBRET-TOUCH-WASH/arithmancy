# ![layerzzzzz](/__prep/docs/assets/cromniomancy.png)

Specifications for the __graphics__ in *Arithmancy*.

At the time of writing, colors from preparatory images/sketches are __not__ to be taken into account.

### Contents
- [Global specifications](#global-specifications)
    <!--- [Resolution](#resolution)-->
    - [Colors](#colors)
    - [Character set](#character-set)
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

For ease of usage, user experience and aesthetic value, *Arithmancy* uses a set of predefined colors ~~totally not taken from [*Dwarf Fortress*](https://dwarffortresswiki.org/index.php/DF2014:Color)~~:

#### *Dark Gray* colors

|Token|RGB|Hex|Sample|
|:-|:-:|:-:|:-:|
|Black|`0,0,0`|`#000000`|![black](/__prep/docs/assets/graphics/colors/black.png)|
|Gray|`128,128,128`|`#808080`|![gray](/__prep/docs/assets/graphics/colors/gray.png)|
|*Taupe*|`72,60,50`|`#483C32`|![taupe](/__prep/docs/assets/graphics/colors/taupe.png)|
|*Charcoal*|`54,69,79`|`#36454F`|![charcoal](/__prep/docs/assets/graphics/colors/charcoal.png)|
|*Taupe* purple|`80,64,77`|`#50404D`|![taupePurple](/__prep/docs/assets/graphics/colors/taupePurple.png)|
|*Taupe* gray|`139,133,137`|`#8B8589`|![taupeGray](/__prep/docs/assets/graphics/colors/taupeGray.png)|

&nbsp;

### *Light Gray* colors

|Token|RGB|Hex|Sample|
|:-|:-:|:-:|:-:|
|*Silver*|`192,192,192`|`#C0C0C0`|![silver](/__prep/docs/assets/graphics/colors/silver.png)|
|*Ash*|`178,190,181`|`#B2BEB5`|![ash](/__prep/docs/assets/graphics/colors/ash.png)|

&nbsp;

#### *White* colors

|Token|RGB|Hex|Sample|
|:-|:-:|:-:|:-:|
|White|`255,255,255`|`#FFFFFF`|![white](/__prep/docs/assets/graphics/colors/white.png)|
|*Beige*|`245,245,220`|`#F5F5DC`|![beige](/__prep/docs/assets/graphics/colors/beige.png)|
|*Ivory*|`255,255,240`|`#FFFFF0`|![ivory](/__prep/docs/assets/graphics/colors/ivory.png)|
|*Lavender*|`255,255,240`|`#E6E6FA`|![lavender](/__prep/docs/assets/graphics/colors/lavender.png)|
|*Lavender blush*|`255,255,240`|`#E6E6FA`|![lavenderBlush](/__prep/docs/assets/graphics/colors/lavenderBlush.png)|


<!--<tbody><tr style="vertical-align: top; padding: 0 1em">
<td>
<table style="text-align: right; border-spacing: 0 1px; margin: 0 auto; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>DGRAY colors</b>
</caption>
<tbody><tr style="background: #808080; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(0, 0, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">BLACK
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#000000
</td></tr>
<tr style="color: white; background: rgb(128, 128, 128)">
<td style="padding: 0.15em 0.4em; text-align: left">CLEAR
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">#808080
</td></tr>
<tr style="color: white; background: rgb(128, 128, 128)">
<td style="padding: 0.15em 0.4em; text-align: left">GRAY
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">#808080
</td></tr>
<tr style="color: white; background: rgb(72, 60, 50)">
<td style="padding: 0.15em 0.4em; text-align: left">TAUPE_DARK
</td>
<td style="padding: 0.15em 0.4em">72
</td>
<td style="padding: 0.15em 0.4em">60
</td>
<td style="padding: 0.15em 0.4em">50
</td>
<td style="padding: 0.15em 0.4em">#483C32
</td></tr>
<tr style="color: white; background: rgb(54, 69, 79)">
<td style="padding: 0.15em 0.4em; text-align: left">CHARCOAL
</td>
<td style="padding: 0.15em 0.4em">54
</td>
<td style="padding: 0.15em 0.4em">69
</td>
<td style="padding: 0.15em 0.4em">79
</td>
<td style="padding: 0.15em 0.4em">#36454F
</td></tr>
<tr style="color: white; background: rgb(80, 64, 77)">
<td style="padding: 0.15em 0.4em; text-align: left">TAUPE_PURPLE
</td>
<td style="padding: 0.15em 0.4em">80
</td>
<td style="padding: 0.15em 0.4em">64
</td>
<td style="padding: 0.15em 0.4em">77
</td>
<td style="padding: 0.15em 0.4em">#50404D
</td></tr>
<tr style="color: black; background: rgb(139, 133, 137)">
<td style="padding: 0.15em 0.4em; text-align: left">TAUPE_GRAY
</td>
<td style="padding: 0.15em 0.4em">139
</td>
<td style="padding: 0.15em 0.4em">133
</td>
<td style="padding: 0.15em 0.4em">137
</td>
<td style="padding: 0.15em 0.4em">#8B8589
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>LGRAY colors</b>
</caption>
<tbody><tr style="background: #C0C0C0">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: black; background: rgb(192, 192, 192)">
<td style="padding: 0.15em 0.4em; text-align: left">SILVER
</td>
<td style="padding: 0.15em 0.4em">192
</td>
<td style="padding: 0.15em 0.4em">192
</td>
<td style="padding: 0.15em 0.4em">192
</td>
<td style="padding: 0.15em 0.4em">#C0C0C0
</td></tr>
<tr style="color: black; background: rgb(178, 190, 181)">
<td style="padding: 0.15em 0.4em; text-align: left">ASH_GRAY
</td>
<td style="padding: 0.15em 0.4em">178
</td>
<td style="padding: 0.15em 0.4em">190
</td>
<td style="padding: 0.15em 0.4em">181
</td>
<td style="padding: 0.15em 0.4em">#B2BEB5
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>WHITE colors</b>
</caption>
<tbody><tr style="background: #FFFFFF">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: black; background: rgb(255, 255, 255)">
<td style="padding: 0.15em 0.4em; text-align: left">WHITE
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">#FFFFFF
</td></tr>
<tr style="color: black; background: rgb(245, 245, 220)">
<td style="padding: 0.15em 0.4em; text-align: left">BEIGE
</td>
<td style="padding: 0.15em 0.4em">245
</td>
<td style="padding: 0.15em 0.4em">245
</td>
<td style="padding: 0.15em 0.4em">220
</td>
<td style="padding: 0.15em 0.4em">#F5F5DC
</td></tr>
<tr style="color: black; background: rgb(255, 255, 240)">
<td style="padding: 0.15em 0.4em; text-align: left">IVORY
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">240
</td>
<td style="padding: 0.15em 0.4em">#FFFFF0
</td></tr>
<tr style="color: black; background: rgb(230, 230, 250)">
<td style="padding: 0.15em 0.4em; text-align: left">LAVENDER
</td>
<td style="padding: 0.15em 0.4em">230
</td>
<td style="padding: 0.15em 0.4em">230
</td>
<td style="padding: 0.15em 0.4em">250
</td>
<td style="padding: 0.15em 0.4em">#E6E6FA
</td></tr>
<tr style="color: black; background: rgb(255, 240, 245)">
<td style="padding: 0.15em 0.4em; text-align: left">LAVENDER_BLUSH
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">240
</td>
<td style="padding: 0.15em 0.4em">245
</td>
<td style="padding: 0.15em 0.4em">#FFF0F5
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>RED colors</b>
</caption>
<tbody><tr style="background: #800000; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(144, 93, 93)">
<td style="padding: 0.15em 0.4em; text-align: left">TAUPE_ROSE
</td>
<td style="padding: 0.15em 0.4em">144
</td>
<td style="padding: 0.15em 0.4em">93
</td>
<td style="padding: 0.15em 0.4em">93
</td>
<td style="padding: 0.15em 0.4em">#905D5D
</td></tr>
<tr style="color: white; background: rgb(128, 0, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">MAROON
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#800000
</td></tr>
<tr style="color: black; background: rgb(184, 115, 51)">
<td style="padding: 0.15em 0.4em; text-align: left">COPPER
</td>
<td style="padding: 0.15em 0.4em">184
</td>
<td style="padding: 0.15em 0.4em">115
</td>
<td style="padding: 0.15em 0.4em">51
</td>
<td style="padding: 0.15em 0.4em">#B87333
</td></tr>
<tr style="color: white; background: rgb(152, 105, 96)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_CHESTNUT
</td>
<td style="padding: 0.15em 0.4em">152
</td>
<td style="padding: 0.15em 0.4em">105
</td>
<td style="padding: 0.15em 0.4em">96
</td>
<td style="padding: 0.15em 0.4em">#986960
</td></tr>
<tr style="color: white; background: rgb(183, 65, 14)">
<td style="padding: 0.15em 0.4em; text-align: left">RUST
</td>
<td style="padding: 0.15em 0.4em">183
</td>
<td style="padding: 0.15em 0.4em">65
</td>
<td style="padding: 0.15em 0.4em">14
</td>
<td style="padding: 0.15em 0.4em">#B7410E
</td></tr>
<tr style="color: white; background: rgb(152, 118, 84)">
<td style="padding: 0.15em 0.4em; text-align: left">PALE_BROWN
</td>
<td style="padding: 0.15em 0.4em">152
</td>
<td style="padding: 0.15em 0.4em">118
</td>
<td style="padding: 0.15em 0.4em">84
</td>
<td style="padding: 0.15em 0.4em">#987654
</td></tr>
<tr style="color: white; background: rgb(150, 113, 23)">
<td style="padding: 0.15em 0.4em; text-align: left">TAUPE_SANDY
</td>
<td style="padding: 0.15em 0.4em">150
</td>
<td style="padding: 0.15em 0.4em">113
</td>
<td style="padding: 0.15em 0.4em">23
</td>
<td style="padding: 0.15em 0.4em">#967117
</td></tr>
<tr style="color: black; background: rgb(145, 129, 81)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_TAN
</td>
<td style="padding: 0.15em 0.4em">145
</td>
<td style="padding: 0.15em 0.4em">129
</td>
<td style="padding: 0.15em 0.4em">81
</td>
<td style="padding: 0.15em 0.4em">#918151
</td></tr>
<tr style="color: white; background: rgb(153, 51, 102)">
<td style="padding: 0.15em 0.4em; text-align: left">MAUVE
</td>
<td style="padding: 0.15em 0.4em">153
</td>
<td style="padding: 0.15em 0.4em">51
</td>
<td style="padding: 0.15em 0.4em">102
</td>
<td style="padding: 0.15em 0.4em">#993366
</td></tr>
<tr style="color: white; background: rgb(178, 0, 75)">
<td style="padding: 0.15em 0.4em; text-align: left">RED_PURPLE
</td>
<td style="padding: 0.15em 0.4em">178
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">75
</td>
<td style="padding: 0.15em 0.4em">#B2004B
</td></tr>
<tr style="color: white; background: rgb(145, 95, 109)">
<td style="padding: 0.15em 0.4em; text-align: left">MAUVE_TAUPE
</td>
<td style="padding: 0.15em 0.4em">145
</td>
<td style="padding: 0.15em 0.4em">95
</td>
<td style="padding: 0.15em 0.4em">109
</td>
<td style="padding: 0.15em 0.4em">#915F6D
</td></tr>
<tr style="color: white; background: rgb(86, 3, 25)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_SCARLET
</td>
<td style="padding: 0.15em 0.4em">86
</td>
<td style="padding: 0.15em 0.4em">3
</td>
<td style="padding: 0.15em 0.4em">25
</td>
<td style="padding: 0.15em 0.4em">#560319
</td></tr>
<tr style="color: white; background: rgb(150, 0, 24)">
<td style="padding: 0.15em 0.4em; text-align: left">CARMINE
</td>
<td style="padding: 0.15em 0.4em">150
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">24
</td>
<td style="padding: 0.15em 0.4em">#960018
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>LRED colors</b>
</caption>
<tbody><tr style="background: #FF0000; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(205, 92, 92)">
<td style="padding: 0.15em 0.4em; text-align: left">CHESTNUT
</td>
<td style="padding: 0.15em 0.4em">205
</td>
<td style="padding: 0.15em 0.4em">92
</td>
<td style="padding: 0.15em 0.4em">92
</td>
<td style="padding: 0.15em 0.4em">#CD5C5C
</td></tr>
<tr style="color: black; background: rgb(244, 194, 194)">
<td style="padding: 0.15em 0.4em; text-align: left">ROSE
</td>
<td style="padding: 0.15em 0.4em">244
</td>
<td style="padding: 0.15em 0.4em">194
</td>
<td style="padding: 0.15em 0.4em">194
</td>
<td style="padding: 0.15em 0.4em">#F4C2C2
</td></tr>
<tr style="color: white; background: rgb(255, 0, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">RED
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#FF0000
</td></tr>
<tr style="color: white; background: rgb(227, 66, 52)">
<td style="padding: 0.15em 0.4em; text-align: left">VERMILION
</td>
<td style="padding: 0.15em 0.4em">227
</td>
<td style="padding: 0.15em 0.4em">66
</td>
<td style="padding: 0.15em 0.4em">52
</td>
<td style="padding: 0.15em 0.4em">#E34234
</td></tr>
<tr style="color: black; background: rgb(233, 116, 81)">
<td style="padding: 0.15em 0.4em; text-align: left">BURNT_SIENNA
</td>
<td style="padding: 0.15em 0.4em">233
</td>
<td style="padding: 0.15em 0.4em">116
</td>
<td style="padding: 0.15em 0.4em">81
</td>
<td style="padding: 0.15em 0.4em">#E97451
</td></tr>
<tr style="color: white; background: rgb(192, 64, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">MAHOGANY
</td>
<td style="padding: 0.15em 0.4em">192
</td>
<td style="padding: 0.15em 0.4em">64
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#C04000
</td></tr>
<tr style="color: white; background: rgb(210, 105, 30)">
<td style="padding: 0.15em 0.4em; text-align: left">CHOCOLATE
</td>
<td style="padding: 0.15em 0.4em">210
</td>
<td style="padding: 0.15em 0.4em">105
</td>
<td style="padding: 0.15em 0.4em">30
</td>
<td style="padding: 0.15em 0.4em">#DC691E
</td></tr>
<tr style="color: black; background: rgb(255, 117, 24)">
<td style="padding: 0.15em 0.4em; text-align: left">PUMPKIN
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">117
</td>
<td style="padding: 0.15em 0.4em">24
</td>
<td style="padding: 0.15em 0.4em">#FF7518
</td></tr>
<tr style="color: black; background: rgb(205, 133, 63)">
<td style="padding: 0.15em 0.4em; text-align: left">LIGHT_BROWN
</td>
<td style="padding: 0.15em 0.4em">205
</td>
<td style="padding: 0.15em 0.4em">133
</td>
<td style="padding: 0.15em 0.4em">63
</td>
<td style="padding: 0.15em 0.4em">#CD853F
</td></tr>
<tr style="color: black; background: rgb(205, 127, 50)">
<td style="padding: 0.15em 0.4em; text-align: left">BRONZE
</td>
<td style="padding: 0.15em 0.4em">205
</td>
<td style="padding: 0.15em 0.4em">127
</td>
<td style="padding: 0.15em 0.4em">50
</td>
<td style="padding: 0.15em 0.4em">#CD7F32
</td></tr>
<tr style="color: black; background: rgb(204, 119, 34)">
<td style="padding: 0.15em 0.4em; text-align: left">OCHRE
</td>
<td style="padding: 0.15em 0.4em">204
</td>
<td style="padding: 0.15em 0.4em">119
</td>
<td style="padding: 0.15em 0.4em">34
</td>
<td style="padding: 0.15em 0.4em">#CC7722
</td></tr>
<tr style="color: black; background: rgb(231, 84, 128)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_PINK
</td>
<td style="padding: 0.15em 0.4em">231
</td>
<td style="padding: 0.15em 0.4em">84
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">#E75480
</td></tr>
<tr style="color: white; background: rgb(220, 20, 60)">
<td style="padding: 0.15em 0.4em; text-align: left">CRIMSON
</td>
<td style="padding: 0.15em 0.4em">220
</td>
<td style="padding: 0.15em 0.4em">20
</td>
<td style="padding: 0.15em 0.4em">60
</td>
<td style="padding: 0.15em 0.4em">#DC143C
</td></tr>
<tr style="color: white; background: rgb(196, 30, 58)">
<td style="padding: 0.15em 0.4em; text-align: left">CARDINAL
</td>
<td style="padding: 0.15em 0.4em">196
</td>
<td style="padding: 0.15em 0.4em">30
</td>
<td style="padding: 0.15em 0.4em">58
</td>
<td style="padding: 0.15em 0.4em">#C41E3A
</td></tr>
<tr style="color: white; background: rgb(255, 36, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">SCARLET
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">36
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#FF0024
</td></tr></tbody></table>
</td>
<td>
<table style="text-align: right; border-spacing: 0 1px; margin: 0 auto; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>BROWN colors</b>
</caption>
<tbody><tr style="background: #808000; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(117, 90, 87)">
<td style="padding: 0.15em 0.4em; text-align: left">RUSSET
</td>
<td style="padding: 0.15em 0.4em">117
</td>
<td style="padding: 0.15em 0.4em">90
</td>
<td style="padding: 0.15em 0.4em">87
</td>
<td style="padding: 0.15em 0.4em">#755A57
</td></tr>
<tr style="color: white; background: rgb(103, 76, 71)">
<td style="padding: 0.15em 0.4em; text-align: left">TAUPE_MEDIUM
</td>
<td style="padding: 0.15em 0.4em">103
</td>
<td style="padding: 0.15em 0.4em">76
</td>
<td style="padding: 0.15em 0.4em">71
</td>
<td style="padding: 0.15em 0.4em">#674C47
</td></tr>
<tr style="color: white; background: rgb(138, 51, 36)">
<td style="padding: 0.15em 0.4em; text-align: left">BURNT_UMBER
</td>
<td style="padding: 0.15em 0.4em">138
</td>
<td style="padding: 0.15em 0.4em">51
</td>
<td style="padding: 0.15em 0.4em">36
</td>
<td style="padding: 0.15em 0.4em">#8A3324
</td></tr>
<tr style="color: white; background: rgb(111, 53, 26)">
<td style="padding: 0.15em 0.4em; text-align: left">AUBURN
</td>
<td style="padding: 0.15em 0.4em">111
</td>
<td style="padding: 0.15em 0.4em">53
</td>
<td style="padding: 0.15em 0.4em">26
</td>
<td style="padding: 0.15em 0.4em">#6F351A
</td></tr>
<tr style="color: black; background: rgb(188, 152, 126)">
<td style="padding: 0.15em 0.4em; text-align: left">TAUPE_PALE
</td>
<td style="padding: 0.15em 0.4em">188
</td>
<td style="padding: 0.15em 0.4em">152
</td>
<td style="padding: 0.15em 0.4em">126
</td>
<td style="padding: 0.15em 0.4em">#BC987E
</td></tr>
<tr style="color: white; background: rgb(101, 67, 33)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_BROWN
</td>
<td style="padding: 0.15em 0.4em">101
</td>
<td style="padding: 0.15em 0.4em">67
</td>
<td style="padding: 0.15em 0.4em">33
</td>
<td style="padding: 0.15em 0.4em">#654321
</td></tr>
<tr style="color: white; background: rgb(112, 66, 20)">
<td style="padding: 0.15em 0.4em; text-align: left">SEPIA
</td>
<td style="padding: 0.15em 0.4em">112
</td>
<td style="padding: 0.15em 0.4em">66
</td>
<td style="padding: 0.15em 0.4em">20
</td>
<td style="padding: 0.15em 0.4em">#704214
</td></tr>
<tr style="color: white; background: rgb(150, 75, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">BROWN
</td>
<td style="padding: 0.15em 0.4em">150
</td>
<td style="padding: 0.15em 0.4em">75
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#964B00
</td></tr>
<tr style="color: white; background: rgb(123, 63, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">CINNAMON
</td>
<td style="padding: 0.15em 0.4em">123
</td>
<td style="padding: 0.15em 0.4em">63
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#7B3F00
</td></tr>
<tr style="color: white; background: rgb(115, 74, 18)">
<td style="padding: 0.15em 0.4em; text-align: left">RAW_UMBER
</td>
<td style="padding: 0.15em 0.4em">115
</td>
<td style="padding: 0.15em 0.4em">74
</td>
<td style="padding: 0.15em 0.4em">18
</td>
<td style="padding: 0.15em 0.4em">#734A12
</td></tr>
<tr style="color: black; background: rgb(181, 166, 66)">
<td style="padding: 0.15em 0.4em; text-align: left">BRASS
</td>
<td style="padding: 0.15em 0.4em">181
</td>
<td style="padding: 0.15em 0.4em">166
</td>
<td style="padding: 0.15em 0.4em">66
</td>
<td style="padding: 0.15em 0.4em">#B5A642
</td></tr>
<tr style="color: white; background: rgb(128, 128, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">OLIVE
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#808000
</td></tr>
<tr style="color: white; background: rgb(85, 104, 50)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_OLIVE
</td>
<td style="padding: 0.15em 0.4em">85
</td>
<td style="padding: 0.15em 0.4em">104
</td>
<td style="padding: 0.15em 0.4em">50
</td>
<td style="padding: 0.15em 0.4em">#556832
</td></tr>
<tr style="color: white; background: rgb(79, 121, 66)">
<td style="padding: 0.15em 0.4em; text-align: left">FERN_GREEN
</td>
<td style="padding: 0.15em 0.4em">79
</td>
<td style="padding: 0.15em 0.4em">121
</td>
<td style="padding: 0.15em 0.4em">66
</td>
<td style="padding: 0.15em 0.4em">#4F7942
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>YELLOW colors</b>
</caption>
<tbody><tr style="background: #FFFF00">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: black; background: rgb(255, 218, 185)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_PEACH
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">218
</td>
<td style="padding: 0.15em 0.4em">185
</td>
<td style="padding: 0.15em 0.4em">#FFDAB9
</td></tr>
<tr style="color: black; background: rgb(210, 180, 140)">
<td style="padding: 0.15em 0.4em; text-align: left">TAN
</td>
<td style="padding: 0.15em 0.4em">210
</td>
<td style="padding: 0.15em 0.4em">180
</td>
<td style="padding: 0.15em 0.4em">140
</td>
<td style="padding: 0.15em 0.4em">#D2B48C
</td></tr>
<tr style="color: black; background: rgb(255, 165, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">ORANGE
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">165
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#FFA500
</td></tr>
<tr style="color: black; background: rgb(255, 229, 180)">
<td style="padding: 0.15em 0.4em; text-align: left">PEACH
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">229
</td>
<td style="padding: 0.15em 0.4em">180
</td>
<td style="padding: 0.15em 0.4em">#FFE5B4
</td></tr>
<tr style="color: black; background: rgb(218, 165, 32)">
<td style="padding: 0.15em 0.4em; text-align: left">GOLDENROD
</td>
<td style="padding: 0.15em 0.4em">218
</td>
<td style="padding: 0.15em 0.4em">165
</td>
<td style="padding: 0.15em 0.4em">32
</td>
<td style="padding: 0.15em 0.4em">#DAA520
</td></tr>
<tr style="color: black; background: rgb(194, 178, 128)">
<td style="padding: 0.15em 0.4em; text-align: left">ECRU
</td>
<td style="padding: 0.15em 0.4em">194
</td>
<td style="padding: 0.15em 0.4em">178
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">#C2B280
</td></tr>
<tr style="color: black; background: rgb(244, 196, 48)">
<td style="padding: 0.15em 0.4em; text-align: left">SAFFRON
</td>
<td style="padding: 0.15em 0.4em">244
</td>
<td style="padding: 0.15em 0.4em">196
</td>
<td style="padding: 0.15em 0.4em">48
</td>
<td style="padding: 0.15em 0.4em">#F4C430
</td></tr>
<tr style="color: black; background: rgb(255, 191, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">AMBER
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">191
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#FFBF00
</td></tr>
<tr style="color: black; background: rgb(212, 175, 55)">
<td style="padding: 0.15em 0.4em; text-align: left">GOLD
</td>
<td style="padding: 0.15em 0.4em">212
</td>
<td style="padding: 0.15em 0.4em">175
</td>
<td style="padding: 0.15em 0.4em">55
</td>
<td style="padding: 0.15em 0.4em">#D4AF37
</td></tr>
<tr style="color: black; background: rgb(240, 234, 214)">
<td style="padding: 0.15em 0.4em; text-align: left">PEARL
</td>
<td style="padding: 0.15em 0.4em">240
</td>
<td style="padding: 0.15em 0.4em">234
</td>
<td style="padding: 0.15em 0.4em">214
</td>
<td style="padding: 0.15em 0.4em">#F0EBD6
</td></tr>
<tr style="color: black; background: rgb(240, 220, 130)">
<td style="padding: 0.15em 0.4em; text-align: left">BUFF
</td>
<td style="padding: 0.15em 0.4em">240
</td>
<td style="padding: 0.15em 0.4em">220
</td>
<td style="padding: 0.15em 0.4em">130
</td>
<td style="padding: 0.15em 0.4em">#F0DC82
</td></tr>
<tr style="color: black; background: rgb(238, 220, 130)">
<td style="padding: 0.15em 0.4em; text-align: left">FLAX
</td>
<td style="padding: 0.15em 0.4em">238
</td>
<td style="padding: 0.15em 0.4em">220
</td>
<td style="padding: 0.15em 0.4em">130
</td>
<td style="padding: 0.15em 0.4em">#EEDC82
</td></tr>
<tr style="color: black; background: rgb(255, 223, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">GOLDEN_YELLOW
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">223
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#FFDF00
</td></tr>
<tr style="color: black; background: rgb(253, 233, 16)">
<td style="padding: 0.15em 0.4em; text-align: left">LEMON
</td>
<td style="padding: 0.15em 0.4em">253
</td>
<td style="padding: 0.15em 0.4em">233
</td>
<td style="padding: 0.15em 0.4em">16
</td>
<td style="padding: 0.15em 0.4em">#FDE910
</td></tr>
<tr style="color: black; background: rgb(255, 253, 208)">
<td style="padding: 0.15em 0.4em; text-align: left">CREAM
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">253
</td>
<td style="padding: 0.15em 0.4em">208
</td>
<td style="padding: 0.15em 0.4em">#FFFDD0
</td></tr>
<tr style="color: black; background: rgb(255, 255, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">YELLOW
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#FFFF00
</td></tr>
<tr style="color: black; background: rgb(204, 255, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">LIME
</td>
<td style="padding: 0.15em 0.4em">204
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#CCFF00
</td></tr>
<tr style="color: black; background: rgb(154, 205, 50)">
<td style="padding: 0.15em 0.4em; text-align: left">YELLOW_GREEN
</td>
<td style="padding: 0.15em 0.4em">154
</td>
<td style="padding: 0.15em 0.4em">205
</td>
<td style="padding: 0.15em 0.4em">50
</td>
<td style="padding: 0.15em 0.4em">#9ACD32
</td></tr>
<tr style="color: black; background: rgb(173, 255, 47)">
<td style="padding: 0.15em 0.4em; text-align: left">GREEN-YELLOW
</td>
<td style="padding: 0.15em 0.4em">173
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">47
</td>
<td style="padding: 0.15em 0.4em">#ADFF2F
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>GREEN colors</b>
</caption>
<tbody><tr style="background: #008000; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(1, 50, 32)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_GREEN
</td>
<td style="padding: 0.15em 0.4em">1
</td>
<td style="padding: 0.15em 0.4em">50
</td>
<td style="padding: 0.15em 0.4em">32
</td>
<td style="padding: 0.15em 0.4em">#013220
</td></tr>
<tr style="color: white; background: rgb(0, 168, 107)">
<td style="padding: 0.15em 0.4em; text-align: left">JADE
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">168
</td>
<td style="padding: 0.15em 0.4em">107
</td>
<td style="padding: 0.15em 0.4em">#00A86B
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>LGREEN colors</b>
</caption>
<tbody><tr style="background: #00FF00">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: black; background: rgb(127, 255, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">CHARTREUSE
</td>
<td style="padding: 0.15em 0.4em">127
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#7BFF00
</td></tr>
<tr style="color: black; background: rgb(0, 255, 0)">
<td style="padding: 0.15em 0.4em; text-align: left">GREEN
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">#00FF00
</td></tr>
<tr style="color: black; background: rgb(80, 200, 120)">
<td style="padding: 0.15em 0.4em; text-align: left">EMERALD
</td>
<td style="padding: 0.15em 0.4em">80
</td>
<td style="padding: 0.15em 0.4em">200
</td>
<td style="padding: 0.15em 0.4em">120
</td>
<td style="padding: 0.15em 0.4em">#50C878
</td></tr>
<tr style="color: black; background: rgb(0, 255, 127)">
<td style="padding: 0.15em 0.4em; text-align: left">SPRING_GREEN
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">127
</td>
<td style="padding: 0.15em 0.4em">#00FF7F
</td></tr></tbody></table>
</td>
<td>
<table style="text-align: right; border-spacing: 0 1px; margin: 0 auto; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>CYAN colors</b>
</caption>
<tbody><tr style="background: #008080; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(46, 139, 87)">
<td style="padding: 0.15em 0.4em; text-align: left">SEA_GREEN
</td>
<td style="padding: 0.15em 0.4em">46
</td>
<td style="padding: 0.15em 0.4em">139
</td>
<td style="padding: 0.15em 0.4em">87
</td>
<td style="padding: 0.15em 0.4em">#2E8B57
</td></tr>
<tr style="color: white; background: rgb(1, 121, 111)">
<td style="padding: 0.15em 0.4em; text-align: left">PINE_GREEN
</td>
<td style="padding: 0.15em 0.4em">1
</td>
<td style="padding: 0.15em 0.4em">121
</td>
<td style="padding: 0.15em 0.4em">111
</td>
<td style="padding: 0.15em 0.4em">#01796F
</td></tr>
<tr style="color: white; background: rgb(0, 128, 128)">
<td style="padding: 0.15em 0.4em; text-align: left">TEAL
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">#008080
</td></tr>
<tr style="color: white; background: rgb(0, 123, 167)">
<td style="padding: 0.15em 0.4em; text-align: left">CERULEAN
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">123
</td>
<td style="padding: 0.15em 0.4em">167
</td>
<td style="padding: 0.15em 0.4em">#007BA7
</td></tr>
<tr style="color: white; background: rgb(0, 51, 102)">
<td style="padding: 0.15em 0.4em; text-align: left">MIDNIGHT_BLUE
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">51
</td>
<td style="padding: 0.15em 0.4em">102
</td>
<td style="padding: 0.15em 0.4em">#003366
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>LCYAN colors</b>
</caption>
<tbody><tr style="background: #00FFFF">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: black; background: rgb(173, 223, 173)">
<td style="padding: 0.15em 0.4em; text-align: left">MOSS_GREEN
</td>
<td style="padding: 0.15em 0.4em">173
</td>
<td style="padding: 0.15em 0.4em">223
</td>
<td style="padding: 0.15em 0.4em">173
</td>
<td style="padding: 0.15em 0.4em">#ADDFAD
</td></tr>
<tr style="color: black; background: rgb(152, 255, 152)">
<td style="padding: 0.15em 0.4em; text-align: left">MINT_GREEN
</td>
<td style="padding: 0.15em 0.4em">152
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">152
</td>
<td style="padding: 0.15em 0.4em">#98FF98
</td></tr>
<tr style="color: black; background: rgb(127, 255, 212)">
<td style="padding: 0.15em 0.4em; text-align: left">AQUAMARINE
</td>
<td style="padding: 0.15em 0.4em">127
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">212
</td>
<td style="padding: 0.15em 0.4em">#7FFFD4
</td></tr>
<tr style="color: black; background: rgb(48, 213, 200)">
<td style="padding: 0.15em 0.4em; text-align: left">TURQUOISE
</td>
<td style="padding: 0.15em 0.4em">48
</td>
<td style="padding: 0.15em 0.4em">213
</td>
<td style="padding: 0.15em 0.4em">200
</td>
<td style="padding: 0.15em 0.4em">#30D5C8
</td></tr>
<tr style="color: black; background: rgb(175, 238, 238)">
<td style="padding: 0.15em 0.4em; text-align: left">PALE_BLUE
</td>
<td style="padding: 0.15em 0.4em">175
</td>
<td style="padding: 0.15em 0.4em">238
</td>
<td style="padding: 0.15em 0.4em">238
</td>
<td style="padding: 0.15em 0.4em">#AFEEEE
</td></tr>
<tr style="color: black; background: rgb(0, 255, 255)">
<td style="padding: 0.15em 0.4em; text-align: left">AQUA
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">#00FFFF
</td></tr>
<tr style="color: black; background: rgb(173, 216, 230)">
<td style="padding: 0.15em 0.4em; text-align: left">LIGHT_BLUE
</td>
<td style="padding: 0.15em 0.4em">173
</td>
<td style="padding: 0.15em 0.4em">216
</td>
<td style="padding: 0.15em 0.4em">230
</td>
<td style="padding: 0.15em 0.4em">#ADD8E6
</td></tr>
<tr style="color: black; background: rgb(135, 206, 235)">
<td style="padding: 0.15em 0.4em; text-align: left">SKY_BLUE
</td>
<td style="padding: 0.15em 0.4em">135
</td>
<td style="padding: 0.15em 0.4em">206
</td>
<td style="padding: 0.15em 0.4em">235
</td>
<td style="padding: 0.15em 0.4em">#87CEEB
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>BLUE colors</b>
</caption>
<tbody><tr style="background: #000080; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(112, 128, 144)">
<td style="padding: 0.15em 0.4em; text-align: left">SLATE_GRAY
</td>
<td style="padding: 0.15em 0.4em">112
</td>
<td style="padding: 0.15em 0.4em">128
</td>
<td style="padding: 0.15em 0.4em">144
</td>
<td style="padding: 0.15em 0.4em">#708090
</td></tr>
<tr style="color: white; background: rgb(0, 71, 171)">
<td style="padding: 0.15em 0.4em; text-align: left">COBALT
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">71
</td>
<td style="padding: 0.15em 0.4em">171
</td>
<td style="padding: 0.15em 0.4em">#0047AB
</td></tr>
<tr style="color: white; background: rgb(0, 0, 139)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_BLUE
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">139
</td>
<td style="padding: 0.15em 0.4em">#00008B
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>LBLUE colors</b>
</caption>
<tbody><tr style="background: #0000FF; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(0, 127, 255)">
<td style="padding: 0.15em 0.4em; text-align: left">AZURE
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">127
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">#007FFF
</td></tr>
<tr style="color: white; background: rgb(0, 0, 255)">
<td style="padding: 0.15em 0.4em; text-align: left">BLUE
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">#0000FF
</td></tr>
<tr style="color: black; background: rgb(204, 204, 255)">
<td style="padding: 0.15em 0.4em; text-align: left">PERIWINKLE
</td>
<td style="padding: 0.15em 0.4em">204
</td>
<td style="padding: 0.15em 0.4em">204
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">#CCCCFF
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>MAGENTA colors</b>
</caption>
<tbody><tr style="background: #800080; color: white">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: white; background: rgb(66, 49, 137)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_VIOLET
</td>
<td style="padding: 0.15em 0.4em">66
</td>
<td style="padding: 0.15em 0.4em">49
</td>
<td style="padding: 0.15em 0.4em">137
</td>
<td style="padding: 0.15em 0.4em">#423189
</td></tr>
<tr style="color: white; background: rgb(49, 0, 98)">
<td style="padding: 0.15em 0.4em; text-align: left">DARK_INDIGO
</td>
<td style="padding: 0.15em 0.4em">49
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">98
</td>
<td style="padding: 0.15em 0.4em">#310062
</td></tr>
<tr style="color: white; background: rgb(75, 0, 130)">
<td style="padding: 0.15em 0.4em; text-align: left">INDIGO
</td>
<td style="padding: 0.15em 0.4em">75
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">130
</td>
<td style="padding: 0.15em 0.4em">#4B0082
</td></tr>
<tr style="color: white; background: rgb(102, 0, 153)">
<td style="padding: 0.15em 0.4em; text-align: left">PURPLE
</td>
<td style="padding: 0.15em 0.4em">102
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">153
</td>
<td style="padding: 0.15em 0.4em">#660099
</td></tr>
<tr style="color: white; background: rgb(102, 0, 102)">
<td style="padding: 0.15em 0.4em; text-align: left">PLUM
</td>
<td style="padding: 0.15em 0.4em">102
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">102
</td>
<td style="padding: 0.15em 0.4em">#660066
</td></tr>
<tr style="color: white; background: rgb(97, 64, 81)">
<td style="padding: 0.15em 0.4em; text-align: left">EGGPLANT
</td>
<td style="padding: 0.15em 0.4em">97
</td>
<td style="padding: 0.15em 0.4em">64
</td>
<td style="padding: 0.15em 0.4em">81
</td>
<td style="padding: 0.15em 0.4em">#614051
</td></tr></tbody></table>
<table style="text-align: right; border-spacing: 0 1px; margin: 1em auto 0; background: black; border-left: 1px solid black; border-right: 1px solid black; width: 100%">
<caption><b>LMAGENTA colors</b>
</caption>
<tbody><tr style="background: #FF00FF">
<th style="text-align: center; padding: 0.15em 0.4em">Token
</th>
<th style="text-align: center; padding: 0.15em 0.4em" colspan="3">RGB
</th>
<th style="text-align: center; padding: 0.15em 0.4em">Hex
</th></tr>
<tr style="color: black; background: rgb(153, 102, 204)">
<td style="padding: 0.15em 0.4em; text-align: left">AMETHYST
</td>
<td style="padding: 0.15em 0.4em">153
</td>
<td style="padding: 0.15em 0.4em">102
</td>
<td style="padding: 0.15em 0.4em">204
</td>
<td style="padding: 0.15em 0.4em">#9966CC
</td></tr>
<tr style="color: white; background: rgb(139, 0, 255)">
<td style="padding: 0.15em 0.4em; text-align: left">VIOLET
</td>
<td style="padding: 0.15em 0.4em">139
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">#8B00FF
</td></tr>
<tr style="color: black; background: rgb(223, 115, 255)">
<td style="padding: 0.15em 0.4em; text-align: left">HELIOTROPE
</td>
<td style="padding: 0.15em 0.4em">223
</td>
<td style="padding: 0.15em 0.4em">115
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">#DF73FF
</td></tr>
<tr style="color: black; background: rgb(200, 162, 200)">
<td style="padding: 0.15em 0.4em; text-align: left">LILAC
</td>
<td style="padding: 0.15em 0.4em">200
</td>
<td style="padding: 0.15em 0.4em">162
</td>
<td style="padding: 0.15em 0.4em">200
</td>
<td style="padding: 0.15em 0.4em">#C8A2C8
</td></tr>
<tr style="color: white; background: rgb(244, 0, 161)">
<td style="padding: 0.15em 0.4em; text-align: left">FUCHSIA
</td>
<td style="padding: 0.15em 0.4em">244
</td>
<td style="padding: 0.15em 0.4em">0
</td>
<td style="padding: 0.15em 0.4em">161
</td>
<td style="padding: 0.15em 0.4em">#F400A1
</td></tr>
<tr style="color: black; background: rgb(204, 136, 153)">
<td style="padding: 0.15em 0.4em; text-align: left">PUCE
</td>
<td style="padding: 0.15em 0.4em">204
</td>
<td style="padding: 0.15em 0.4em">136
</td>
<td style="padding: 0.15em 0.4em">153
</td>
<td style="padding: 0.15em 0.4em">#CC8899
</td></tr>
<tr style="color: black; background: rgb(255, 192, 203)">
<td style="padding: 0.15em 0.4em; text-align: left">PINK
</td>
<td style="padding: 0.15em 0.4em">255
</td>
<td style="padding: 0.15em 0.4em">192
</td>
<td style="padding: 0.15em 0.4em">203
</td>
<td style="padding: 0.15em 0.4em">#FFC0CB
</td></tr>
<tr style="color: black; background: rgb(250, 218, 221)">
<td style="padding: 0.15em 0.4em; text-align: left">PALE_PINK
</td>
<td style="padding: 0.15em 0.4em">250
</td>
<td style="padding: 0.15em 0.4em">218
</td>
<td style="padding: 0.15em 0.4em">221
</td>
<td style="padding: 0.15em 0.4em">#FADADD
</td></tr>
<tr style="color: black; background: rgb(221, 173, 175)">
<td style="padding: 0.15em 0.4em; text-align: left">PALE_CHESTNUT
</td>
<td style="padding: 0.15em 0.4em">221
</td>
<td style="padding: 0.15em 0.4em">173
</td>
<td style="padding: 0.15em 0.4em">175
</td>
<td style="padding: 0.15em 0.4em">#DDADAF
</td></tr></tbody></table>
</td></tr></tbody>-->
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