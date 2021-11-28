#!usr/bin/env python

"""
board.py: does stuff
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"

import logging

# Constants
LOG_NAME = "board"
SIZE = 10
TILE_MISS = -1
DISPLAY_MISS = 'O'
TILE_EMPTY = 0
DISPLAY_EMPTY = ' '
TILE_HIT = 1
DISPLAY_HIT = 'X'
ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
NEWLINE = '\n'
WRAP_CHAR = '*'
SPACE = ' '

# Global variables
log = logging.getLogger(LOG_NAME)


def main():
    b = Board()
    b.display()


def wrap(notification):
    """
    Formats a text string to be surrounded with a specified character for visibility in massive
    walls of text
    :param notification: The text string to be formatted
    :return: The formatted text string
    """
    length = len(notification)
    msg = NEWLINE
    # Construct first line
    i = 0
    while i < (length + 4):  # Buffer 2 extra chars on either side for border
        msg += WRAP_CHAR
        i += 1
    msg += NEWLINE
    # Construct second line
    i = 0
    msg += WRAP_CHAR + SPACE
    while i < length:
        msg += SPACE
        i += 1
    msg += SPACE + WRAP_CHAR + NEWLINE
    # Construct third line
    msg += WRAP_CHAR + SPACE + notification + SPACE + WRAP_CHAR + NEWLINE
    # Construct fourth line
    i = 0
    msg += WRAP_CHAR + SPACE
    while i < length:
        msg += SPACE
        i += 1
    msg += SPACE + WRAP_CHAR + NEWLINE
    # Construct fifth line
    i = 0
    while i < (length + 4):  # Buffer 2 extra chars on either side for border
        msg += WRAP_CHAR
        i += 1
    msg += NEWLINE
    return msg


class Board(object):
    def __init__(self):
        self.data = [[TILE_EMPTY for i in range(SIZE)] for j in range(SIZE)]
        log.debug("New board created")

    def display(self):
        output = "   "
        for letter in ROWS:
            output += f"{letter} "
        output += NEWLINE
        for i, row in enumerate(self.data):
            output += f"{i + 1:<2d} "
            for value in row:
                if value is TILE_MISS:
                    output += DISPLAY_MISS
                elif value is TILE_HIT:
                    output += DISPLAY_HIT
                elif value is TILE_EMPTY:
                    output += DISPLAY_EMPTY
                output += SPACE
            output += NEWLINE
        print(output)

    def get(self):
        return

    def is_empty(self):
        return

    def shoot(self, x, y):
        """
        Shoots the specified (x, y) coordinate on the board.
        :param x: x-coord
        :param y: y-coord
        :return: TILE_HIT if hit, TILE_MISS if miss, None if invalid
        """
        if self.data is None:
            log.warning("Board data not initialized")
            return None
        elif x not in range(SIZE) or y not in range(SIZE):
            log.warning("Invalid coordinates")
            return None
        else:
            return self.data[x][y]


if __name__ == "__main__":
    main()
