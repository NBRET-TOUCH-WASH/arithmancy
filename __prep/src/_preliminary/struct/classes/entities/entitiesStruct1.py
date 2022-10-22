#coding:utf-8

"""
$ 2022-09-22 ; 22:24
    $ this is a first draft/attempt at creating the class structure of the game
    $ said structure is fully documented in `__prep\docs\struct\Entities.md`
"""

from abc import ABC, abstractmethod



class IMagicUser:
    """\"Interface\" used for entities versed in the art of magic"""

    def __init__(self):
        self.mp = 0
        self._maxMp = 0


    def _getMaxMp(self):
        return self._maxMp
    def _setMaxMp(self):
        print("The maximum amount of MP cannot be changed after initialization.")

    maxMp = property(_getMaxMp, _setMaxMp)



class Entity:
    """\"Abstract\" class whom every entity sub-class inherits from"""

    def __init__(self):
        self.name = "Toto, Bearer of Galaxies"
        self.hp = 0
        self._maxHp = 0

    def move(self):
        pass

    def attack(self):
        pass


    def _getMaxHp(self):
        return self._maxHp
    def _setMaxHp(self):
        print("The maximum amount of HP cannot be changed after initialization.")

    maxHp = property(_getMaxHp, _setMaxHp)



class Player(Entity):
    """\"Abstract\" class whom derived player character classes inherit from"""

    def _setName(self):
        pass

    name = property(_getName, _setName)


class Warrior(Player):
    pass

class Mage(Player):
    pass