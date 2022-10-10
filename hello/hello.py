#!/usr/bin/env python3

"""
Stanford CS106A Hello Example.
Use as an example for the command line.
Use to test that Python is working on a machine.
"""

import sys


def main():
    args = sys.argv[1:]  # standard - load "args" list with cmd-line-args

    # -d debug mode, print diagnostics about args then exit.
    if len(args) >= 1 and args[0] == '-d':
        print('number of args:', len(args))
        print('list of args:', args)
        return

    # 0 args - print 'Hello World'
    if len(args) == 0:
        print('Hello World')

    # 1 arg - print 'Hello arg'
    if len(args) == 1:
        print('Hello', args[0])

    # 3 args
    # -n NN arg - print N copies of arg
    if len(args) == 3 and args[0] == '-n':
        n = int(args[1])
        name = args[2]
        for i in range(n):
            # print a space after instead of \n
            print(name, end=' ')
        print()  # one \n at the end


# Python boilerplate.
if __name__ == '__main__':
    main()
