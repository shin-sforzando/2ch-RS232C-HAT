#!/usr/bin/env python3

import curses
import time

import pysnooper

from src import logger_timing


@pysnooper.snoop()
@logger_timing()
def main() -> None:
    """The main function as an entry point.

    Todo:
        - Rewrite the actual logics.
    """
    try:
        stdscr = curses.initscr()
        curses.noecho()
        for t in range(10):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Program will be terminated after {10-t} [s].")
            stdscr.refresh()
            time.sleep(1)
    except KeyboardInterrupt:
        raise
    finally:
        curses.echo()
        curses.endwin()


if __name__ == "__main__":
    main()
