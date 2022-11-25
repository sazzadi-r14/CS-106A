#!/usr/bin/env python3

"""
Stanford CS106A Pylibs Example
Nick Parlante
"""

import sys
import random

def read_terms(filename):
    """
    Given the filename of the terms file, read
    it into a dict with each 'noun' word as a key
    and its value is its list of subs ['apple', 'donut', 'unicorn'].
    Return the terms dict.
    >>> read_terms('test-terms.txt')
    {'noun': ['cat', 'donut', 'velociraptor'], 'verb': ['nap', 'run']}
    """
    terms = {}
    with open(filename) as f:
        for line in f:
            # line is: noun,apple,rabbit,velociraptor,balloon
            line = line.strip()  # remove \n
            parts = line.split(',')
            term = parts[0]    # 'noun'
            words = parts[1:]  # ['apple', 'rabbit' ..]
            terms[term] = words
    return terms


def substitute(terms, word):
    """
    Given terms dict and a word from the template.
    Return the substituted form of that word.
    If it is of the form '[noun]' return a random
    word from the terms dict. Otherwise
    return the word unchanged.
    >>> substitute({'noun': ['apple']}, '[noun]')
    'apple'
    >>> substitute({'noun': ['apple']}, 'donut')
    'donut'
    """
    if word.startswith('[') and word.endswith(']'):
        word = word[1:len(word) - 1]  # trim off [ ]
        if word in terms:
            subs = terms[word]  # list ['apple', 'donut', ..]
            return random.choice(subs)
    return word


def process_template(terms, filename):
    """
    Given terms dict and filename of template.
    Process the template file, printing out its lines
    with the substitution done.
    """
    with open(filename) as f:
        for line in f:
            # split() no param = splits on whitespace chars
            words = line.split()  # ['I', 'had', 'a', '[noun]']
            # Print each word with substitution done
            for word in words:
                sub = substitute(terms, word)
                # Print word without a newline
                print(sub + ' ', end='')
            # Print 1 newline after all the words
            print()


def main():
    args = sys.argv[1:]

    # command line: terms-file template-file
    pass
    if len(args) == 2:
        terms = read_terms(args[0])
        process_template(terms, args[1])


if __name__ == '__main__':
    main()
