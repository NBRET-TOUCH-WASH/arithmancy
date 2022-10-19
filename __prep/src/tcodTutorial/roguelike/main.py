#coding:utf-8

import tcod

from engine import Engine
from entity import Entity
from procgen import generate_dungeon
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    tileset = tcod.tileset.load_tilesheet("assets/tilesheet160x160.png", 16,16, tcod.tileset.CHARMAP_CP437)

    event_handler = EventHandler()

    player = Entity(40,25, '@', (255,255,255))
    npc = Entity(25,25, '☻', (0,128,128))
    entities = {player, npc}

    game_map = generate_dungeon(max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player, engine_name="Fox Engine")

    with tcod.context.new_terminal(
        screen_width,
        screen_height,

        tileset=tileset,
        title="Preparatory phase tcod handling",
        vsync=True

    ) as context:

        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            engine.handle_events(events)



if __name__ == "__main__":
    main()