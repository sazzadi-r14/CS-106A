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
    >>> pix_dist2((3, 4, 7), (14, 24, 29))
    1005
    >>> pix_dist2((4, 20, 9), (8, 24, 53))
    1968
    """

    return (pix1[0] - pix2[0]) ** 2 + (pix1[1] - pix2[1]) ** 2 + (pix1[2] - pix2[2]) ** 2  # Implementing the eqn


def avg_pixl(pixs):
    """
    Returns a tuple of the average rgb values from a list of pixels
    >>> avg_pixl([(18, 18, 18), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 2, 0), (1, 0, 1)])
    (13.166666666666666, 13.333333333333334, 13.166666666666666)
    >>> avg_pixl([(14, 23, 20), (24, 18, 53), (13, 18, 29), (4, 7, 33), (42, 47, 50), (80, 5, 9)])
    (29.5, 19.666666666666668, 32.333333333333336)
    """
    # Creating a variable get the sum of all the colors.
    red = 0
    green = 0
    blue = 0
    total = len(pixs)
    for pixel in pixs:
        red += pixel[0]
        green += pixel[1]
        blue += pixel[2]

    avg = (red / total, green / total, blue / total)  # Calculates the average of all values, and stores it in a tuple.
    return avg


def best_pix(pixs):
    """
    Given a list of 1 or more pix, returns the best pix.

    >>> best_pix([(1, 1, 1), (1, 1, 1), (28, 28, 28)])
    (1, 1, 1)
    >>> best_pix([(14, 24, 9), (20, 23, 24), (29, 53, 24)])
    (20, 23, 24)
    >>> best_pix([(59, 39, 42), (38, 54, 6), (9, 18, 33)])
    (38, 54, 6)
    >>> best_pix([(59, 39, 42), (10, 18, 32), (9, 18, 33)])
    (10, 18, 32)
    >>> best_pix([(36, 54, 7), (38, 54, 6), (9, 18, 33)])
    (36, 54, 7)
    """
    avg = avg_pixl(pixs)
    return min(pixs, key=lambda pixel: pix_dist2(pixel, avg))  # Returns the closest tuple to average.


def good_apple_pix(pixs):
    """
    Given a list of 2 or more pix, return the best pix
    according to the good-apple strategy.
    >>> good_apple_pix([(18, 18, 18), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 2, 0), (1, 0, 1)])
    (20, 20, 20)
    """
    avg = avg_pixl(pixs)
    srt_lst = sorted(pixs, key=lambda pixel: pix_dist2(pixel, avg))
    return best_pix(srt_lst[:len(srt_lst) // 2])  # Uses the best_pix function for good half.


def lst_pixl(images, x, y, mode):
    """
    This helper function takes a list of images and returns the best pixel tuple of a particular co-ordinate.
    """
    pixel_lst = []
    for image in images:
        pixel_lst.append(image.get_pix(x, y))  # This builds a list of tuples for the specific pixel of all the photos.
    # Instead of putting the argument in solve, putting it here made it easier to execute this code.
    if mode == None:
        return best_pix(pixel_lst)
    elif mode == '-good':
        return good_apple_pix(pixel_lst)


def solve(images, mode):
    """
    Given a list of image objects and mode,
    compute and show a Ghost solution image based on these images.
    Mode will be None or '-good'.
    There will be at least 3 images, and they will all be
    the same size.
    """
    # Classic blank image building algorithm, just using the tuple technique in less lines.
    width = images[0].width
    height = images[0].height
    solution = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pix = lst_pixl(images, x, y, mode)
            solution.set_pix(x, y, pix)
    solution.show()


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
