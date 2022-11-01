#coding:utf-8

#type checking
from typing import Tuple

#classes
class Color:
    """Class allowing for the creation of predefined color tokens.\n
    Instances are not subject to changes during execution. Would be coded as a `struct` in languages like C#."""

    def __init__(self, rgb:Tuple[int,int,int]) -> None:
        self.rgb = rgb

        #? has no use as of writing
        self.hex = (hex(self.rgb[0]), hex(self.rgb[1]), hex(self.rgb[2]))

        self.cap_values()



    def __repr__(self) -> str:
        return f"RGB: {self.rgb} | HEX: {self.hex}"



    def cap_values(self) -> None:
        """Safety function used to ensure a color isn't \
        set to be darker or lighter than physically possible \
        (respectively `BLACK` & `WHITE`).\n
        Returns nothing (`None`)."""

        for channel in self.rgb:
            if channel < 0:
                channel = 0

            elif channel > 255:
                channel = 255