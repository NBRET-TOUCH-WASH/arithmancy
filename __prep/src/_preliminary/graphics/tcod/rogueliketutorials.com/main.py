#coding:utf-8

#modules
from logging import root
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler

#modules init

#functions
def main() -> None:
    #screen dimensions
    screen_width = 80
    screen_height = 50
    #good tested out values:
    #screen_width = 115
    #screen_height = 65



    #tileset
    tileset = tcod.tileset.load_tilesheet("font/dejavuFont.png", 32,8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(1,1, '@', (255,255,255))
    npc = Entity(10,15, 'g', (255,0,0))
    entities = {npc, player}

    engine = Engine(entities, event_handler, player)



    #terminal init
    with tcod.context.new_terminal(
        screen_width, screen_height,
        tileset = tileset,
        title = "Tcod lib roguelike test °1",
        vsync = True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order='F')



        while True:
            engine.render(root_console, context)

            events = tcod.event.wait()
            engine.handle_events(events)

#script

#execution
if __name__ == "__main__":
    main()

#$ 2022-10-02 ; 23:30
    #$ was about to create class map according to tutorial (part7)