#!/usr/bin/env python3

"""
Stanford CS106A BabyNames Project
Part-A: organizing the bulk data
"""

import sys


def add_name(names, year, rank, name):
    """
    Add the given data: int year, int rank, str name
    to the given names dict and return it.
    (1 test provided, more tests TBD)
    >>> add_name({}, 2000, 10, 'Abe')
    {'Abe': {2000: 10}}
    >>> add_name({'Abe': {2000: 10}}, 2010, 20, 'Abe')
    {'Abe': {2000: 10, 2010: 20}}
    >>> add_name({'Abe': {2000: 10}}, 2000, 10, 'Abe')
    {'Abe': {2000: 10}}
    >>> add_name({'Abe': {2000: 10}}, 2000, 178, 'Abe')
    {'Abe': {2000: 10}}
    >>> add_name({'Abe': {2000: 178}}, 2000, 10, 'Abe')
    {'Abe': {2000: 10}}
    """

    date = {}  # The empty string to store the year: rank dict
    if name in names:  # If the name is already in the dictionary then assigns the dictionary under the name key to date
        date = names[name]
    if year in date:
        if date[year] > rank:  # If there is same name, it chooses to stck with the higher rank.
            date[year] = rank
    if year not in date:  # If the year is not in the key, then adds the year and rank to the date dict
        date[year] = rank
        # print(date)
        # print(name)
        # print(names)
    names[name] = date  # Assigns the final dictionary of date to the dictionary.

    return names


def add_file(names, filename):
    """
    Given a names dict and babydata.txt filename, add the file's data
    to the dict and return it.
    (Tests provided, Code TBD)
    >>> add_file({}, 'small-2000.txt')
    {'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}
    >>> add_file({}, 'small-2010.txt')
    {'Yot': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Alice': {2010: 2}}
    >>> add_file({'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}, 'small-2010.txt')
    {'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena': {2010: 1}}
    """
    with open(filename) as f:
        for line in f:
            line = line.strip()
            lst_line = line.split(',')  # Splitting the string about the commas, and storing the list in a variable.
            if len(lst_line) == 1:  # This if statement just takes the year out of the first step of the loop.
                year = lst_line[0]
            else:  # For all the other cases than the first one.
                add_name(names, int(year), int(lst_line[0]), lst_line[1])  # Adding male names to the dict
                add_name(names, int(year), int(lst_line[0]), lst_line[2])  # Adding female names to the dict
    return names


def read_files(filenames):
    """
    Given list of filenames, build and return a names dict
    of all their data.
    """
    names = {}
    for i in range(len(filenames)):  # Iterate through the list of files and adds the data to the dictionary.
        add_file(names, filenames[i])

    return names


def search_names(names, target):
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    Not case sensitive.
    (Code and tests TBD)
    >>> search_names({'Yot': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Alice': {2010: 2}}, 'o')
    ['Bob', 'Yot']
    >>> search_names({'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena':{2010: 1}}, 'A')
    ['Alice', 'Zena']
    >>> search_names({'Raaida': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Saazzad': {2000: 2}, 'Yot': {2010: 1}, 'Aamir':{2010: 1}}, 'Aa')
    ['Aamir', 'Raaida', 'Saazzad']
    
    """
    name = []
    for key in names:  # Loops through all the keys of the dictionary
        if target.lower() in key.lower():  # Turns everything into lower case and looks if the substring is in key.
            name.append(key)  # Adds everything to the list.
    name.sort()  # Sorts the entire list.
    return name


def print_names(names):
    """
    (provided)
    Given names dict, print out all its data, one name per line.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Change filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
