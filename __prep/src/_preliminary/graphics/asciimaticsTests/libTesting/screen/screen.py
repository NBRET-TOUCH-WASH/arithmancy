#coding:utf-8

#modules
from asciimatics.screen import Screen
from time import sleep

#functions
def main(screen:Screen):
    screen.clear()
    screen.print_at("Hello World!", 0,0)

    screen.refresh()
    sleep(3)
    screen.clear_buffer()

#script
Screen.wrapper(main)