#coding:utf-8

"""
$ 2022-09-22 ; 22:57
    $ this is a second draft/attempt at creating the class structure of the game
    $ said structure is fully documented in `__prep\docs\struct\Entities.md`
"""

class IMagicUser:
    """\"Interface\" used for entities versed in the art of magic"""

    def __init__(self):
        self.mp = 0
        self.maxMp = 0

    def CastSpell(self):
        pass


class Entity:
    """\"Abstract\" base class whom every entity sub-class inherits from."""

    def __init__(self):
        self.name = "John Place"
        self.hp = 0
        self.maxHp = 0

    def move(self):
        pass

    def attack(self):
        pass



class Player(Entity):
    """\"Abstract\" class whom derived player character classes inherit from."""

    def __init__(self):
        Entity.__init__(self)

        self.gender = "Agender"
        self.level = 1

    def level_up(self):
        pass


class Warrior(Player):
    """`Warrior` character class.\n
    Specializes in raw strength."""

    def __init__(self):
        self.rageCharges = 1

    def level_up(self):
        """`level_up` method override from the `Player` base class."""
        pass

    def enrage(self):
        #§TOADD: self.rageCharges -= 1
        pass

    def attack(self):
        """`attack` method override from the `Player` base class."""
        pass


class Mage(Player, IMagicUser):
    """`Mage` character class.\n
    Specializes in magic/spellcasting."""

    def __init__(self):
        pass

    def attack(self):
        """`attack` method override from the `Player` base class."""
        pass