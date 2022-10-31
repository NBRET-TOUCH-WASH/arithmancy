#coding:utf-8

"""
$ 2022-09-23 ; 13:56
    $ this is a third attempt at entities classes structure
"""

class IMagicUser:
    def __init__(self) -> None:
        self.mp = 0
        self.maxMp = 0

    def cast_spell():
        pass


class IFecalFunny:
    def __init__(self) -> None:
        self.smell = "odorless"

    def flatulate():
        pass

    def defecate():
        pass



class Entity:
    def __init__(self) -> None:
        self.name = "John Place"
        self.hp = 0
        self.maxHp = 0

    def move():
        pass

    def attack():
        pass



class Player(Entity):
    def __init__(self) -> None:
        #used to set an "empty" default character gender
        self.gender = "Agender"
        self.level = 1

    def move(self):
        print(f"{self.name} walks around aimlessly...")

    def level_up():
        pass


class Warrior(Player):
    def __init__(self) -> None:
        self.name = "John Angery"
        #used to set an "empty" default character gender
        self.gender = "Agender"
        self.level = 1

        self.maxHp = 120
        self.hp = self.maxHp

        self.rage_charges = 1

    def __repr__(self) -> str:
        return f"\"{self.name}\", a Level {self.level} Warrior ({self.maxHp} HP)"

    def attack(self):
        print(f"{self.name} slashes the enemy to ribbons!")

    def enrage(self):
        print(f"{self.name} is now enraged!")

    def level_up(self):
        self.level += 1
        print(f"{self.name} is now a Level {self.level} Warrior!")


class Mage(Player, IMagicUser):
    def __init__(self) -> None:
        #used to set an "empty" default character gender
        self.gender = "Agender"
        self.level = 1
        self.name = "Gringledoof"

        self.maxHp = 100
        self.hp = self.maxHp

        self.maxMp = 80
        self.mp = self.maxMp

    def __repr__(self) -> str:
        return f"\"{self.name}\", a Level {self.level} Mage ({self.maxHp} HP | {self.maxMp} MP)"

    def attack(self):
        print(f"{self.name} BONKS the enemy in the head with their magic wand!")

    def level_up(self):
        self.level += 1
        print(f"{self.name} is now a Level {self.level} Mage!")

    def cast_spell(self):
        print(f"{self.name} (Level {self.level} Mage) casts a spell using their magic wand!")



class Creature(Entity):
    pass


class Blob(Creature):
    def __init__(self) -> None:
        self.name = "Blob"
        self.color = (255,255,255)

    def move(self):
        print(f"{self.name} slobbers all over you.")

    def attack(self):
        print(f"{self.name} violently pukes corrosive slime on your body!")


class ShartBlob(Blob, IFecalFunny):
    def __init__(self) -> None:
        self.name = "Shart"

        self.color = (128,64,0)

    def attack(self):
        print(f"{self.name} violently pukes corrosive faeces on your body!")

    def flatulate(self):
        print(f"{self.name} flatulates loudly.")

    def defecate(self):
        print(f"{self.name} defecates, letting you on a dreadful sight.")


class Skeleton(Creature):
    def __init__(self) -> None:
        self.name = "Skeleton"

    def attack(self):
        print(f"{self.name} uses one of their own bones as a club and hits you with it!")


class SpookySkeleton(Skeleton):
    def __init__(self) -> None:
        self.name = "Mr. Skeltal"

    def agonize(self):
        print(f"In agony, {self.name} lets out an ear-shattering screech before dying!")


class SpoopySkeleton(Skeleton, IFecalFunny):
    def __init__(self) -> None:
        self.name = "Necromantic spooper"
        self.smell = "rotten eggs"

    def flatulate(self):
        print(f"{self.name} \"flatulates\" by compressing one of their ribs. You feel like you're gonna be sick...")

    def defecate(self):
        print(f"{self.name} \"defecates\" by swallowing dirt. You wonder what is wrong with them...")



#==========#

warrior_char = Warrior()
print(warrior_char)
warrior_char.level_up()

mage_char = Mage()
print(mage_char)
mage_char.cast_spell()

skeltal_char = SpookySkeleton()
skeltal_char.agonize()

spoop_char = SpoopySkeleton()
spoop_char.flatulate()