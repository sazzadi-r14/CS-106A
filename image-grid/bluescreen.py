#!/usr/bin/env python3

#Story Behind This picture
""""
My picture might not be the most artisitic one. But, this is as close to my heart as it could 
be. I always love astronomy, and it was kind of hoplessly romantic to me. So, I always kept the
stargazing thingy deeply personal to me. Because I wanted to stargaze only with the person I'm sure about. 
When I found my fiancee Orion was the first constellation that we looked at. Which is the background of the image. 
I always loved Astronautics. That's why she gav eme a tiny astronaut around the beginning of our relationship. 
WHich is the foreground. The background of Orion Constellation that you see, was hand drawn by her. I'm 13 thousand
kilometers away from her now. But, I always keep these with me. So, I though what can be a better use of these stuffs 
than this homework? Nevermind, the best of these are in the heart. Thank you so much for going through this. 

"""


"""
Stanford Bluescreen Example
Shows front and back strategies
The functions are mostly complete,
missing only the key if-logic line.

Please see the handout for an explanation of the
two strategies.

Front strategy. For this strategy, the back image
must be at least as large as the front image.
args: front-img back-img
$ python3 bluescreen.py monkey-500.jpg moon-600.jpg
$ python3 bluescreen.py monkey-500.jpg stanford-600.jpg

Back strategy.
args: front-img shift-x shift-y back-img
$ python3 bluescreen.py monkey-500.jpg 200 50 stanford-600.jpg
"""

import sys
from simpleimage import SimpleImage


def do_front(front_filename, back_filename):
    """
    Front strategy: loop over front image,
    detect blue pixels there,
    substitute in pixels from back.
    Return changed front image.
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3

            # Your code - replace False with expression
            # detect pixels in front that should be replaced with back pixels
            if pixel.green > average * 1.15:    
                back_pixel = back.get_pixel(x, y)
                pixel.red = back_pixel.red * 0.8
                pixel.green = back_pixel.green * 0.8
                pixel.blue = back_pixel.blue * 0.8
    return image


def do_back(front_filename, shift_x, shift_y, back_filename):
    """
    Back strategy: loop over image,
    detect *non-blue* pixels.
    Copy those pixels to back, shifted by shift_x, shift_y.
    Pixels which fall outside of the background are ignored.
    Return changed back image.
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    # Loop over front image - copy non-blue pixels
    # to backkground
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3

            # Your code - replace False with expression
            # detect pixels in front that should be copied to back
            if pixel.green < average * 1.1:
                dest_x = x + shift_x
                dest_y = y + shift_y
                # Only copy pixels to back if they will be in-bounds
                if back.in_bounds(dest_x, dest_y):
                    back_pixel = back.get_pixel(dest_x, dest_y)
                    back_pixel.red = pixel.red * 0.8
                    back_pixel.green = pixel.green * 0.8
                    back_pixel.blue = pixel.blue * 0.8
    return back



def main():
    args = sys.argv[1:]

    # args:
    # front-image back-image                 - do front strategy
    # front-image shift-x shift-y back-image - do back strategy

    if len(args) != 2 and len(args) != 4:
        print('Args not recognized. Usage:')
        print('2 args for front strategy:')
        print('  front-image back-image')
        print('4 args for back strategy:')
        print('  front-image shift-x shift-y back-image')
        return

    if len(args) == 2:
        image = do_front(args[0], args[1])
        image.show()

    if len(args) == 4:
        image = do_back(args[0], int(args[1]), int(args[2]), args[3])
        image.show()


if __name__ == '__main__':
    main()
