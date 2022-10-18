#coding:utf-8

#modules
from time import sleep

from asciimatics.screen import Screen
from asciimatics.widgets.frame import Frame

from asciimatics.widgets.layout import Layout
from asciimatics.widgets.button import Button

#script
def func(screen:Screen):
    screen.clear()

    frame = Frame(screen, 80,20, has_border=True)
    layout = Layout([1,1,1,1])
    frame.add_layout(layout)

    layout.add_widget(Button("haha :)", None), 0)
    layout.add_widget(Button("hoho :(", None), 3)

    screen.refresh()
    sleep(3)

Screen.wrapper(func)