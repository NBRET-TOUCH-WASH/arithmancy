#coding:utf-8

import urwid

hello_world_txt = urwid.Text(u"Hello World!")
text_fill = urwid.Filler(hello_world_txt, "top")
main_loop = urwid.MainLoop(text_fill)

main_loop.run()