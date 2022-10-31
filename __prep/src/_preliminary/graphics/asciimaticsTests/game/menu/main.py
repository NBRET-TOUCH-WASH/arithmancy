#coding:utf-8

#modules
from asciimatics.screen import *

from asciimatics.widgets import *
from asciimatics.widgets.frame import *
from asciimatics.widgets.layout import *


from menu import *

#functions
def main(stdscr:Screen):
    stdscr.clear()
    while True:
        stdscr.clear_buffer(stdscr.COLOUR_DEFAULT, stdscr.A_NORMAL, stdscr.COLOUR_DEFAULT)

        frame = Frame(stdscr, 80, 20, has_border=False)
        layout = Layout([1, 1, 1, 1])
        frame.add_layout(layout)

        stdscr.refresh()

#script
Screen.wrapper(main)