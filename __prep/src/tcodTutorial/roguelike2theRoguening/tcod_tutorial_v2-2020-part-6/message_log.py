#coding:utf-8

from typing import List, Reversible, Tuple
import textwrap

import tcod

import color



class Message:
    def __init__(self, text:str, fg:Tuple[int, int, int]) -> None:
        self.plain_text = text
        self.fg = fg
        self.count = 1

    @property
    def full_text(self) -> str:
        """The message's full text, including `count` if necessary"""
        if self.count > 1:
            return f"{self.plain_text} (x{self.count})"
        return self.plain_text


class MessageLog:
    def __init__(self) -> None:
        self.messages : List[Message] = []

    def add_message(self, text:str, fg:Tuple[int,int,int]=color.white, *, stack:bool=True) -> None:
        """Adds a message to this log.\n
        `text` is the message's text, `fg` its foreground (text) color.\n
        If `stack` is `True` then the messages can stack with the previous message of the same text."""

        if stack and self.messages and text == self.messages[-1].plain_text:
            self.messages[-1].count += 1
        else:
            self.messages.append(Message(text, fg))

    def render(self, console:tcod.Console, x:int, y:int, width:int, height:int) -> None:
        """Render this log over the given area.
        `x`, `y`, `width`, `height` is the rectangular region to render onto
        the `console`.
        """

        self.render_messages(console, x,y, width,height, self.messages)

    @staticmethod
    def render_messages(console:tcod.Console, x:int, y:int, width:int, height:int, messages:Reversible[Message]) -> None:
        """Render the messages provided.
        The `messages` are rendered starting at the last message and working
        backwards.
        """

        y_offset = height -1
        for message in reversed(messages):
            for line in reversed(textwrap.wrap(message.full_text, width)):
                console.print(x,y + y_offset, line, message.fg)
                y_offset -= 1
                if y_offset < 0:
                    return  # No more space to print messages.