#coding:utf-8

from entity import Entity

player = Entity(char="@", color=(255,255,255), name="Player", blocks_movement=True)

orc = Entity(char="o", color=(128,255,0), name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(0,255,128), name="Troll", blocks_movement=True)