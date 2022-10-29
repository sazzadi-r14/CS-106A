#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def compute_slug(key):
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    slug = []
    conv_key = key.lower()
    for i in range(len(key)):
        if conv_key[i].isalpha() and conv_key[i] not in slug: #To add the key
            slug.append(conv_key[i])
    for j in range(len(ALPHABET)): #To add the alphabet
        if ALPHABET[j] not in slug: 
            slug.append(ALPHABET[j])

    return slug


def encrypt_char(source, slug, ch):
    """
    Given source and slug lists,
    if the char ch is in source, return
    its encrypted form. Otherwise return ch unchanged.
    >>> # Compute 'z' slug, store it in a var named z_slug
    >>> # and pass that in as the slug for the tests.
    >>> z_slug = compute_slug('z')
    >>> encrypt_char(ALPHABET, z_slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, z_slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, z_slug, 'D')
    'C'
    >>> encrypt_char(ALPHABET, z_slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, z_slug, ' ')
    ' '
    """
    if ch.isalpha():
        if ch.lower() in source:
            i = source.index(ch.lower())
            if ch.isupper():
                return slug[i].upper() #Returns upper case
            else:
                return slug[i] # Returns lower case
    return ch


def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> z_slug = compute_slug('z')
    >>> encrypt_str(ALPHABET, z_slug, 'And like a thunderbolt he falls.')
    'Zmc khjd z sgtmcdqanks gd ezkkr.'
    """
    encrypted_str = ''
    for i in range(len(s)):
        encrypted_str += encrypt_char(source, slug, s[i])

    return encrypted_str


def decrypt_str(source, slug, s):
    """
    Given source and slug lists and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.')
    'And like a thunderbolt he falls.'
    """
    decrypted = encrypt_str(slug, source, s) # Had fun using this argument

    return decrypted


def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    slug = compute_slug(key)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(encrypt_str(ALPHABET, slug, line))


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    slug = compute_slug(key)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(decrypt_str(ALPHABET, slug, line))


def main():
    args = sys.argv[1:]
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.
    if len(args) == 3 and args[0] == '-encrypt':
        encrypt_file(args[2], args[1])
    
    if len(args) == 3 and args[0] == '-decrypt':
        decrypt_file(args[2], args[1])

#That was the meanest thing you guys could do. You all really shouldn't have rickrolled us after
#hours of insane hardowrk.

#Cardinal-Red

# Python boilerplate.
if __name__ == '__main__':
    main()
