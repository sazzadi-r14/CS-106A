#!/usr/bin/env python3

"""
Stanford CS106A Crazycat Example
Like the "cat" utility that prints out a file
with a couple added features. The code here
is complete.
Nick Parlante

3 Command line argument forms:
  filename
  -crazy filename
  -vowels filename

Demonstrates file-reading and printing like "cat".
Demonstrates a main() that looks at command line arg strings.
The -crazy and -vowels features show string functions
with Doctests.
Changed to use line.strip() to get rid of '\n' endings.
"""

import sys


def print_file_plain(filename):
    """
    Given a filename, read all its lines and print them out.
    This shows our standard file-reading loop.
    """
    with open(filename) as f:
        for line in f:
            line = line.strip()   # remove \n
            print(line)


def crazy_str(s):
    """
    Given a string s, return a crazy looking version where the first
    char is lowercase, the second is uppercase, the third is lowercase,
    and so on. So 'Hello' returns 'hElLo'.
    >>> crazy_str('Hello')
    'hElLo'
    >>> crazy_str('@xYz!')
    '@XyZ!'
    >>> crazy_str('')
    ''
    """
    result = ''
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result


def print_file_crazy(filename):
    """
    Given a filename, read all its lines and print them out
    in crazy form.
    """
    with open(filename) as f:
        for line in f:
            line = line.strip()
            crazy = crazy_str(line)
            print(crazy)
            # could combine above - dense:
            # print(crazy_str(line))


def count_vowels(s):
    """
    Given a string of text, returns the
    count of 'a' 'e' 'i' 'o' 'u' in line.
    Not case sensitive.
    >>> count_vowels('xxaeiouxx')
    5
    >>> count_vowels('AaEEEU')
    6
    >>> count_vowels('')
    0
    """
    count = 0
    # Convert whole line to lower, maybe easier
    # than converting each char to lower one at a time.
    s = s.lower()
    for i in range(len(s)):
        # Trick: use "in" replacing low=='a' or low=='e'...
        if s[i] in 'aeiou':
            count += 1
    return count


def print_file_vowels(filename):
    """
    Given a filename, read and print out all its lines,
    including the vowel-count with each line.
    """
    with open(filename) as f:
        for line in f:
            line = line.strip()
            vowels = count_vowels(line)
            print(vowels, line)


def main():
    args = sys.argv[1:]
    # Code here looks at command line arguments and calls functions
    # filename -> calls print_file_plain()
    # -crazy filename -> calls print_file_crazy()
    # -vowels filename -> calls print_file_vowels()
    if len(args) == 1:
        # args[0] is filename
        print_file_plain(args[0])

    if len(args) == 2 and args[0] == '-crazy':
        print_file_crazy(args[1])

    if len(args) == 2 and args[0] == '-vowels':
        print_file_vowels(args[1])


# Standard call-main() boilerplate at end of file.
if __name__ == '__main__':
    main()
