#!/usr/bin/env python3

"""
Stanford CS106A TipTop Project
"""

import sys


def read_file(filename):
    """
    This function takes the file in and creates the dictionary.
    """
    tags_dict = {}
    # Boiler Plate file reader algorithm.
    with open(filename) as f:
        for line in f:
            line = line.strip()
            parts = line.split('^')  # Splits the line about '^'.
            poster = parts[0].lower()  # Sets the poster string to a variable from the list's index 0.
            tags_lst = parts[1:]  # Creates a list of the tags.
            for tag in tags_lst:  # Iterates through the list of tags.
                tag = tag.lower()
                if tag not in tags_dict:  # Classic nested list in dictionary algorithm.
                    tags_dict[tag] = []
                poster_lst = tags_dict[tag]  # Assigning the list of posters to a variable.
                if poster not in poster_lst:
                    poster_lst.append(poster)
    return tags_dict


def dict_printer(tags_dict):
    """
    This function goes through the entire dictionary and prints them accordingly.
    """
    keys = tags_dict.keys()  # Created a list of keys.
    sorted_keys = sorted(keys)  # Sorts the list of keys.
    for key in sorted_keys:  # Printing loop.
        print(key)
        poster_lst = tags_dict[key]  # Takes access of the poster's list through the key.
        sorted_poster = sorted(poster_lst)  # Sorts the poster's list.
        for poster in sorted_poster:
            print(poster)


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        tags_dict = read_file(args[0])
        dict_printer(tags_dict)


if __name__ == '__main__':
    main()
