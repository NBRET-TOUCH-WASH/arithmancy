#coding:utf-8

#modules
from asciimatics import *
from asciimatics.screen import *

#functions
def main(screen:Screen):
    player_x = 0
    player_y = 0

    screen.clear()
    while True:
        screen.clear_buffer(screen.COLOUR_DEFAULT, screen.A_NORMAL, screen.COLOUR_DEFAULT)

        screen.print_at("@", player_x,player_y, screen.A_BOLD, screen.COLOUR_RED)

        screen.refresh()
        user_event:KeyboardEvent = screen.get_event()
        if user_event == None:
            continue
        elif user_event.key_code == ord('q'):
            player_x -= 1
        elif user_event.key_code == ord('d'):
            player_x += 1
        elif user_event.key_code == ord('z'):
            player_y -= 1
        elif user_event.key_code == ord('s'):
            player_y += 1

#script
Screen.wrapper(main)