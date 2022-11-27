#!/usr/bin/env python3

"""
Stanford CS106A WordCount Example
Nick Parlante

Counting the words in a text file is a sort
of Rosetta Stone of programming - it uses files, dicts, functions,
loops, logic, decomposition, testing, command line in main().
Trace the flow of data starting with main().
There is a sorted/lambda exercise below.

Code is provided for alphabetical output like:
$ python3 wordcount.py somefile.txt
aardvark 1
anvil 3
boat 4
...

**Exercise**

Implement code in print_top() to print the n most common words,
using sorted/lambda/items.

Then command line -top n feature calls print_top() for output like:
$ python3 wordcount.py -top 10 alice-book.txt
the 1639
and 866
to 725
a 631
she 541
it 530
of 511
said 462
i 410
alice 386
"""

import sys


def clean(s):
    """
    Given string s, returns a clean version of s where all non-alpha
    chars are removed from beginning and end, so '@@hi^^' yields 'hi'.
    The resulting string will be empty if there are no alpha chars.
    >>> clean('$abc^')      # basic
    'abc'
    >>> clean('abc$$')
    'abc'
    >>> clean('^x^')        # short (debug)
    'x'
    >>> clean('abc')        # edge cases
    'abc'
    >>> clean('$$$')
    ''
    >>> clean('')
    ''
    """
    # Move begin rightwards, past non-alpha punctuation
    begin = 0
    while begin < len(s) and not s[begin].isalpha():
        begin += 1

    # Move end leftwards, past non-alpha
    end = len(s) - 1
    while end >= begin and not s[end].isalpha():
        end -= 1

    # begin/end cross each other -> nothing left
    if end < begin:
        return ''
    return s[begin:end + 1]


def read_counts(filename):
    """
    Given filename, reads its text, splits it into words.
    Returns a "counts" dict where each word
    is the key and its value is the int count
    number of times it appears in the text.
    Converts each word to a "clean", lowercase
    version of that word.
    The Doctests use little files like "test1.txt" in
    this same folder.
    >>> read_counts('test1.txt')
    {'a': 2, 'b': 2}
    >>> read_counts('test2.txt')    # Q: why is b first here?
    {'b': 1, 'a': 2}
    >>> read_counts('test3.txt')
    {'bob': 1}
    """
    with open(filename) as f:
        text = f.read()  # read file as string vs for/line/in way

    # .split() with no parameters splits on whitespace,
    # and \n counts as whitespace, so get whole file
    # ['Roses', 'are', 'red', 'Violets', 'are', ...]
    words = text.split()

    counts = {}
    for word in words:
        word = word.lower()
        cleaned = clean(word)  # style: call clean() once, store in var
        if cleaned != '':      # subtle - cleaning may leave only ''
            if cleaned not in counts:
                counts[cleaned] = 0
            counts[cleaned] += 1
    return counts


def print_counts(counts):
    """
    Given counts dict, print out each word and count
    one per line in alphabetical order, like this
    aardvark 1
    apple 13
    ...
    """
    for word in sorted(counts.keys()):
        print(word, counts[word])
    # Alternately can use counts.items() to access all key/value pairs
    # in one step.
    # for key, value in sorted(counts.items()):
    #    print(key, value)


def print_top(counts, n):
    """
    (Exercise)
    Given counts dict and int n, print the n most common words
    in decreasing order of count
    the 1639
    and 866
    to 725
    ...
    """
    items = counts.items()
    # To get a start writing the code, could print raw items to
    # get an idea of what we have.
    # print(items)

    # Your code here - our solution is 3 lines long, but it's dense!
    # Hint:
    # Sort the items with a lambda so the most common words are first.
    # Then print just the first n word,count pairs
    pass


def main():
    # (provided)
    # Command line forms
    # 1. filename
    # 2. -top n filename   # prints n most common words
    args = sys.argv[1:]

    if len(args) == 1:
        # filename
        counts = read_counts(args[0])
        print_counts(counts)

    if len(args) == 3 and args[0] == '-top':
        # -top n filename
        n = int(args[1])
        counts = read_counts(args[2])
        print_top(counts, n)


if __name__ == '__main__':
    main()
