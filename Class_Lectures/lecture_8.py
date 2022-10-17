# https://web.stanford.edu/class/cs106a/handouts_w2021/lecture-8.html



# String Index
"""
to loop over Index numbers
"""
range(len(s))

for i in range(len(s)):
    s[i]

# Charracter class test

    """_summary_
    sapce, new line \n, tab\t
    
    Finding only alphabets from all the other kind of 
    chars
    """
def alpha_only(s):
    alphabet = ''
    for i in range(len(s)):
        char = s[i]
        if char.isalpha():
            alphabet += char
           
    return alphabet


# If in depth

if test-expression:
    lines_t # run if test True
else:
    lines-F # runs if test False
    
# Early-Return Strategy

# Doctest
    >>> digits_only('Hi4!x3')
    '43'
    >>> digits_only('123')
    '123'
    >>> digits_only('xyz')
    ''
    >>> digits_only('')
    ''
result = ''
for i in range(len(s)):
    if s[i].isdigit():
        result += s[i]
return result

Just a change so I can push from 