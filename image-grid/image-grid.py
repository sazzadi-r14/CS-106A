#!/usr/bin/env python3

"""
Stanford CS106A Image Grid Project
"""

import sys
import random

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def draw_image(image, out, left, top, mode):
    """
    #Draw a copy of "image" into "out", with image's origin
    #at (left, top) within the out image.
    #Mode is one of 'red' 'green' 'blue' 'all',
    #ontrolling which colors of each pixel are copied.
    #(See handout for details)
    """
    width = image.width
    height = image.height
    
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            position = out.get_pixel(left + x, top + y)
            if mode == 'red':
                position.red = pixel.red
            if mode == 'green':
                position.green = pixel.green
            if mode == 'blue':
                position.blue = pixel.blue
            if mode == 'all':
                position.red = pixel.red
                position.green = pixel.green
                position.blue = pixel.blue


def make_channels(filename):
    """
    Given an image filename.
    Creates an out image with 3x the width,
    filled with the red, green, and blue channels
    of the original image.
    """
    image = SimpleImage(filename)
    # Specifying 'black' as the color for the blank image.
    out = SimpleImage.blank(image.width * 3, image.height, back_color='black')
    
    width = image.width
    height = image.height
    
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            #Red Channel
            red_channel = out.get_pixel(x, y)
            red_channel.red = pixel.red
            red_channel.green = pixel.green * 0 
            red_channel.blue = pixel.blue * 0
            #Green Channel
            green_channel = out.get_pixel(x + width, y)
            green_channel.red = pixel.red * 0
            green_channel.green = pixel.green
            green_channel.blue = pixel.blue * 0
            #Blue Channel
            blue_channel = out.get_pixel(x + (width * 2), y)
            blue_channel.red = pixel.red * 0
            blue_channel.green = pixel.green * 0
            blue_channel.blue = pixel.blue
            
    # Draw out image on screen
    out.show()


def make_test(filename):
    """
    Uses draw_image() to create a larger blue background
    with the image centered on it as a basic test.
    (provided code)
    """
    image = SimpleImage(filename)
    top_margin = 20
    side_margin = 40
    out = SimpleImage.blank(image.width + side_margin * 2, image.height + top_margin * 2, back_color='blue')
    draw_image(image, out, side_margin, top_margin, 'all')
    out.show()

def make_grid(filename, n, plain):
    """
    Create an n x n grid image of the given image filename.
    If plain is True, the images are copied plain.
    If plain is False, random color versioss of each
    are used.
    (provided code)
    """
    image = SimpleImage(filename)
    out = SimpleImage.blank(image.width * n, image.height * n, back_color='black')
    # Row and col numbers identify the individual rows and columns
    # e.g. 3 columns would use numbers 0, 1, 2
    for row in range(n):
        for col in range(n):
            # Based on row/col numbers compute the left/top of each image
            if plain:
                draw_image(image, out, col * image.width, row * image.height, 'all')
            else:
                # This selects one of the colors at random
                choice = random.choice(['red', 'green', 'blue'])
                draw_image(image, out, col * image.width, row * image.height, choice)
    out.show()


def main():
    # (provided)
    args = sys.argv[1:]

    # -hello name
    if len(args) == 2 and args[0] == '-hello':
        print("Everything's coming up", args[1] + '!')

    # -test img
    if len(args) == 2 and args[0] == '-test':
        make_test(args[1])

    # -channels img
    if len(args) == 2 and args[0] == '-channels':
        make_channels(args[1])

    # -grid img n
    if len(args) == 3 and args[0] == '-grid':
        n = int(args[2])
        make_grid(args[1], n, True)

    # -random img n
    if len(args) == 3 and args[0] == '-random':
        n = int(args[2])
        make_grid(args[1], n, False)


if __name__ == '__main__':
    main()
