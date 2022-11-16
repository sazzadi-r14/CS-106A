#!/usr/bin/env python3

"""
Stanford CS106A Draw1 Project
Nick Parlante
Examples + Exercises for DrawCanvas drawing
"""

import sys
from drawcanvas import DrawCanvas


MARGIN = 20


def draw_redx(canvas, left, top, width, height):
    """
    Given a canvas and left,right and width,height.
    Draw the "redx" figure with that location and size.
    (this code is complete)
    """
    # Draw outer rectangle
    canvas.draw_rect(left, top, width, height)

    # Draw oval set in by 20 pixels all around.
    # What is upper left corner x,y of the oval?
    # What is its width,height?
    canvas.fill_oval(left + 20, top + 20, width - 40, height - 40, color='yellow')

    # Draw 2 lines of red X
    # upper-left to lower-right
    canvas.draw_line(left, top, left + width - 1, top + height - 1, color='red')

    # lower-left to upper-right
    canvas.draw_line(left, top + height - 1, left + width - 1, top, color='red')

    # Note: better style would be to have a MARGIN constant = 20, and the oval line
    # is as below. We used 20 above to keep the example simple. We'll use constants
    # like this on a later homework.
    # canvas.fill_oval(left + MARGIN, right + MARGIN, width - 2 * MARGIN, height - 2 * MARGIN, color='yellow')


def draw_lines1(canvas, left, top, width, height, n):
    """
    Draw the lines1 figure within left,top .. width,height
    (this code is complete)
    """
    canvas.draw_rect(left, top, width, height)
    # Figure y_add for each i in the loop
    for i in range(n):
        y_add = (i / (n - 1)) * (height - 1)  # formula: fraction * max
        canvas.draw_line(left, top, left + width - 1, top + y_add, color='red')


def draw_lines2(canvas, left, top, width, height, n):
    """
    Draw the lines2 figure within left,top .. width,height
    The code for lines1 is already here
    """
    canvas.draw_rect(left, top, width, height)

    for i in range(n):
        y_add = (i / (n - 1)) * (height - 1)  # formula: 0..1 fraction * max
        canvas.draw_line(left, top, left + width - 1, top + y_add, color='red')

    # loop to draw green "lines2" lines
    for i in range(n):
        y_add = (i / (n - 1)) * (height - 1)
        # Your code here - work out x_add and draw each green line
        pass


def draw_grid1(width, height, n):
    """
    Creates a canvas of the given size.
    Draws a grid1 of n-by-n black rectangles
    (this code is complete)
    """
    canvas = DrawCanvas(width, height, title='Draw1')

    # Figure sizes for all sub rects
    sub_width = width // n
    sub_height = height // n

    # Loop over row/col
    for row in range(n):
        for col in range(n):
            # Figure upper left of this sub rect
            left = col * sub_width
            top = row * sub_height
            canvas.draw_rect(left, top, sub_width, sub_height)
            # Can try different colors, oval .. whatever we put here,
            # we get n * n copies of it.


def draw_grid2(width, height, n):
    """
    Creates a canvas of the given size.
    Add code to draw the lines2 figure in each grid sub rect.
    """
    canvas = DrawCanvas(width, height, title='Draw1')

    sub_width = width // n
    sub_height = height // n

    for row in range(n):
        for col in range(n):
            # Compute left,top in pixels of this row,col
            left = col * sub_width
            top = row * sub_height
            # Your code here - draw a lines2 figure in each grid rect
            pass


# main() code is complete.
# There are 6 command lines that work here,
# with width/height/n being positive integers.
#  -first
#  -redx width height
#  -lines1 width height n
#  -lines2 width height n
#  -grid1 width height n
#  -grid2 width height n
# e.g. run like this in the terminal:
#  python3 draw1.py -lines1 600 400 10


def main():
    # Standard first line of main to get args
    args = sys.argv[1:]

    # The command-line parsing here is not a good example
    # of command line parsing - more complex than usual

    # Do this one first - does not use width/height command line

    width = 500
    height = 300
    # Parse width/height/n from command line, giving a helpful
    # error message if it fails.
    if len(args) > 1:
        try:
            width = int(args[1])
            height = int(args[2])
        except Exception:
            print("Error parsing int width/height from command line:" + ' '.join(args))
            return

    # Tricky: we do all the drawing in a try, so that if it takes an exception,
    # we can still do the mainloop() at the end. If we do not do this, an exception
    # causes no graphics output to appear which makes debugging hard.
    try:
        if args[0] == '-first':
            # Create 500 by 300 canvas
            canvas = DrawCanvas(500, 300)
            # Draw filled blue oval
            canvas.fill_oval(100, 50, 200, 50, color='blue')
            # Note: color= is an optional, named parameter
            # passed in to the function call.

        if args[0] == '-redx':
            canvas = DrawCanvas(width * 2, height * 2, fast_draw=True, title='Draw1')
            # Can change to fast_draw=False .. drawing plays out more slowly
            draw_redx(canvas, 0, 0, width, height)
            draw_redx(canvas, width, height, width, height)

        if args[0] == '-lines1':
            canvas = DrawCanvas(width * 2, height * 2, fast_draw=True, title='Draw1')
            n = int(args[3])
            draw_lines1(canvas, 0, 0, width, height, n)
            draw_lines1(canvas, width, height, width, height, n)

        if args[0] == '-lines2':
            canvas = DrawCanvas(width * 2, height * 2, fast_draw=True, title='Draw1')
            n = int(args[3])
            draw_lines2(canvas, 0, 0, width, height, n)
            draw_lines2(canvas, width, height, width, height, n)

        if args[0] == '-grid1':
            n = int(args[3])
            draw_grid1(width, height, n)

        if args[0] == '-grid2':
            n = int(args[3])
            draw_grid2(width, height, n)

    # Print out exception from draw
    except Exception as e:
        print(e)

    DrawCanvas.mainloop()


if __name__ == '__main__':
    main()
