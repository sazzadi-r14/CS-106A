import sys
import math

FRUITS = [('banana', 0.45, 6), ('jackfruit', 4.55, 2), ('kiwi', 0.15, 23)]


def prices(lst):
    
    prices = []
    for tuple in lst:
        prices.append(tuple[1])
    
    print(prices)


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        if args[0] == 'prices':
            prices(FRUITS)
        elif args[0] == 'prices':
            

if __name__ == '__main__':
    main()