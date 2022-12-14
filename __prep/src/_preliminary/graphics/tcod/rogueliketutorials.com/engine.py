#coding:utf-8

from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler



class Engine:
    def __init__(self, entities:Set[Entity], event_handler:EventHandler, player: Entity) -> None:
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    def handle_events(self, events:Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                self.player.move(action.dx, action.dy)

            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def render(self, console:Console, context:Context):
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, entity.color)

        context.present(console)
        console.clear()