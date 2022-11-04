#coding:utf-8

#type checking
from tcod import Console

#classes
class Options:
    """Options list class"""

    def __init__(self,
                console:Console,
                options:list=["☺ Beget ☻","§ About §","☼ Options ☼","¥ Forfare ¥"]) -> None:
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


    def print_options(self, console:Console, screen_width:int, screen_height:int, selected_row:int):
        console.draw_frame((screen_width//2) - self.width//2,
                                    (screen_height//2) - self.height//2,
                                    self.width,
                                    self.height)


        #the row on which the "next" option text is printed on
        row = 1
        for opt in self.options:
            #if the currently printed row is the one "selected" by the user, highlight it
            if row == selected_row:
                console.print((screen_width//2) - len(opt)//2,
                                (screen_height//2) - self.height//2 + row + 2,
                                opt, (0,0,0), (255,255,255))

            #if the currently printed row is not the one "selected" by the user, do not highlight it
            else:
                console.print((screen_width//2) - len(opt)//2,
                                (screen_height//2) - self.height//2 + row + 2,
                                opt)
            row += 1