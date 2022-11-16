#!/usr/bin/env python3

"""
Trying out drawings using simpledraw layer

Next:
 skyline?
 draw_quilt/grid type with fn call
 integrate with server .. maybe return canvas?

"""
import sys
import tkinter
import random

from drawcanvas import DrawCanvas

import datetime

from pdb import set_trace as st


# Some of the TK color names
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple',
          'cyan', 'dark green', 'pink', 'black']


def draw_arrow(canvas, x, y, length, flex):
    """
    Draw a horizontal line with arrow heads at both ends.
    It's left endpoint at x,y, extending for length pixels.
    "flex" is 0.0 .. 1.0, the fraction of length that the arrow
    heads should extend horizontally.
    """
    # Compute where the line ends, draw it
    x_right = x + length - 1
    canvas.draw_line(x, y, x_right, y)

    # Draw 2 arrowhead lines, up and down from left endpoint
    head_len = flex * length
    canvas.draw_line(x, y, x + head_len, y - head_len)  # up
    canvas.draw_line(x, y, x + head_len, y + head_len)  # down

    # Draw 2 arrowhead lines from the right endpoint
    # your code here
    pass


def draw_arrows(width, height, flex, trick=False):
    canvas = DrawCanvas(width, height)

    # Arrow length is half width
    length = width * 0.5
    # Position it at 25% of width and height
    x = width * 0.25
    y = height * 0.25
    draw_arrow(canvas, x, y, length, flex)

    # Trick mode: make flex negative
    if trick:
        flex = flex * -1

    y2 = height * 0.75
    draw_arrow(canvas, x, y2, length, flex)



def main():
    args = sys.argv[1:]
    # Arg forms:
    # -bars n
    # -pyramid n
    # -nest n

    # Figure window size (default 500 x 300)
    # Optionally command line can have width height numbers to override
    # e.g. -bars 10 1000 500
    width = 500
    height = 300
    if len(args) == 4:
        width = int(args[-2])
        height = int(args[-1])

    if len(args) >= 2 and args[0] == '-arrows':
        draw_arrows(width, height, float(args[1]))

    if len(args) >= 2 and args[0] == '-trick':
        draw_arrows(width, height, float(args[1]), trick=True)

    DrawCanvas.mainloop()



if __name__ == '__main__':
    main()
