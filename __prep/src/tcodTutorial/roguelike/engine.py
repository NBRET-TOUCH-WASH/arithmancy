#cooding:utf-8

from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from game_map import GameMap
from entity import Entity
from input_handlers import EventHandler



class Engine:
    def __init__(self, entities:Set[Entity], event_handler:EventHandler, game_map:GameMap, player:Entity, engine_name:str = None) -> None:
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.name = engine_name

    def handle_events(self, events:Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console:Console, context:Context) -> None:
        self.game_map.render(console)
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, entity.color)

        context.present(console)
        console.clear()