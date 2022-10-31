#coding:utf-8

#type checking
from tcod import Console

class Options:
    """Options list class"""

    def __init__(self,
                console:Console,
                options:list=["Beget","About","Options","Forfare"]) -> None:
        self.options = options
        self.set_required_space(console)



    def set_required_space(self, console:Console) -> None:
        """Calculates the required space to draw the options text (includes margins from frame).\n
        Returns nothing (`None`), only defines instance attributes."""

        #WHYNOT: only use `self.width` instead of `max_x` and `self.height` instead of `max_y`
            #µ because it doesn't fucking work, dumbass
                #&=> nevermind it works now lol

        self.width:int = 0
        self.height:int = 0

        for opt in self.options:
            if len(opt) > self.width:
                self.width = len(opt)
        self.width += 6

        self.height:int = len(self.options)
        self.height += 6