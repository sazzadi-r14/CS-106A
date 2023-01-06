import sys
import math

FRUITS = [('banana', 0.45, 6), ('jackfruit', 4.55, 2), ('kiwi', 0.15, 23)]

P1 = {'Jenny': 8675309, 'Julia': 2124320, 'Kylie': 4602121, 'Sonja': 4444444,
      'Nick': 8080543}
P2 = {'Logan': 6202121, 'Jeff': 8888888, 'Nick': 8080543, 'Kylie': 4602121,
      'Sonja': 4444444, 'Jenny': 2128765}


def prices(lst):
    prices = []
    for tuple in lst:
        prices.append(tuple[1])

    print(prices)


def mutual_friends(p1, p2):
    """
    >>> mutual_friends(P1, P2)
    {'Kylie': 4602121, 'Sonja': 4444444, 'Nick': 8080543}
    """
    mutual_friends = {}
    for first in p1:
        if first in p2:
            if p1[first] == p2[first]:
                mutual_friends[first] = p1[first]
    return mutual_friends


def get_word_to_prevs(words):
    """
    >>> all_words = ['all', 'is', 'well', 'that', 'ends', 'well', 'that']
    >>> get_word_to_prevs(all_words)
    {'is': ['all'], 'well': ['is', 'ends'], 'that': ['well'], 'ends': ['that']}
    """
    result = {}
    for i in range(1, len(words)):
        word = words[i]
        if word not in result:
            result[word] = []
        lst = result[word]
        if words[i - 1] not in lst:
            lst.append(words[i - 1])
    return result


def count_zips(filename):
    states = {}
with open(filename) as f:
    for line in f:
        line = line.strip()
        big_lst = line.split(',')
        if big_lst[0] not in states:
            states[big_lst[0]] = {}
        for i in range(1, len(big_lst)):
            small_lst = big_lst[i].split('-')
           fasf



def main():
    args = sys.argv[1:]
    if len(args) == 1:
        if args[0] == 'prices':
            prices(FRUITS)
        elif args[0] == 'prices':
            pass


if __name__ == '__main__':
    main()
