#coding:utf-8

#modules
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText

#functions
def demo(screen:Screen):
    effects = [
        Cycle(screen,
            FigletText("Hello","epic"),
            screen.height//2 - 8),
        Cycle(screen,
            FigletText("World!", "epic"),
            screen.height//2 + 3),

        Stars(screen, (screen.width + screen.height)//2)
    ]

    screen.play([Scene(effects, 500)])

#script
Screen.wrapper(demo)