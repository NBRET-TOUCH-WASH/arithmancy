#coding:utf-8

"""
"""

#modules
import curses
from curses import wrapper

#modules init
stdscr = curses.initscr()

#functions
def main(stdscr=stdscr):
    curses.endwin()

#script
wrapper(main)