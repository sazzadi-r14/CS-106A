#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    """
    pass


def best_pix(pixs):
    """
    Given a list of 1 or more pix, returns the best pix.
    """
    pass


def good_apple_pix(pixs):
    """
    Given a list of 2 or more pix, return the best pix
    according to the good-apple strategy.
    >>> good_apple_pix([(18, 18, 18), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 2, 0), (1, 0, 1)])
    (20, 20, 20)
    """
    pass


def solve(images, mode):
    """
    Given a list of image objects and mode,
    compute and show a Ghost solution image based on these images.
    Mode will be None or '-good'.
    There will be at least 3 images and they will all be
    the same size.
    """
    pass


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage.file(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # Command line args
    # 1 arg:  dir-of-images
    # 2 args: -good dir-of-images
    if len(args) == 1:
        images = load_images(args[0])
        solve(images, None)

    if len(args) == 2 and args[0] == '-good':
        images = load_images(args[1])
        solve(images, '-good')


if __name__ == '__main__':
    main()
