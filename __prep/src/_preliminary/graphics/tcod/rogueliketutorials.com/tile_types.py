#coding:utf-8

from typing import Tuple
import numpy

graphic_dt = numpy.dtype(
    [
        ("ch", numpy.int32),
        ("fg", "3B"),
        ("bg", "3B")
    ]
)

tile_dt = numpy.dtype(
    [
        ("walkable", numpy.bool8),
        ("transparent", numpy.bool8),
        ("dark", graphic_dt)
    ]
)


def new_tile(*,
    walkable:int,
    transparent:int,
    dark:Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> numpy.ndarray:
    """Helper function to define individual tile types"""
    return numpy.array((walkable, transparent, dark), tile_dt)

floor = new_tile(walkable=True, transparent=True, dark=(ord("+"), (255,255,255), (50, 50, 150)))
wall = new_tile(walkable=False, transparent=False, dark=(ord("#"), (255,255,255), (0,0,100)))