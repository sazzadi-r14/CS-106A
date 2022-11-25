#Class Notes

for ch in s:
    result = ch + ch

lst[]
lst.index()
lst.append()

#Alright let's start with string find

string_var.find() #Anything in this function give out the index value of the particular strin gthat I am searching for. 
>>> s = 'Python'
>>> 
>>> s.find('th')
2
>>> s.find('o')
4
>>> s.find('y')
1
>>> s.find('x')
-1
>>> s.find('N')
-1
>>> s.find('P')
0

#In depth view at the function

s.find(target, start_index)

>>> s = '[xyz['
>>> s.find('[')      # find first [
0
>>> s.find('[', 1)   # start search at 1
4

# String Slicing
>>> s = 'Python'
>>> s[1:3]    # 1 .. UBNI
'yt'
>>> s[1:5]
'ytho'
>>> s[4:5]
'o'
>>> s[4:4]    # "not including" dominates
''

>>> s[:3]     # omit = from/to end
'Pyt'
>>> s[4:]
'on'
>>> s[4:999]  # too big = through the end
'on'
>>> s[:4]     # "perfect split" on 4
'Pyth'
>>> s[4:]
'on'
>>> s[:]      # the whole thing
'Python'

# Now here comes the part of case sensivity. 

s.upper() s.lower() s.isupper() s.islowe>>> 'Kitten123'.upper()  # return with all chars in upper form
'KITTEN123'
>>> 'Kitten123'.lower()
'kitten123'
>>> 
>>> 'a'.islower()
True
>>> 'A'.islower()
False
>>> 'A'.isupper()
True
>>> '@'.islower()
False
>>> 'a'.upper()
'A'
>>> 'A'.upper()
'A'
>>> '@'.upper()
'@'

#Lecture 16

def while_double(s):
    result = ''
i = 0
while i < len(s):
    result += s[i] + s[i]
    i += 1
return result




dict.keys()

returns a list of the keys

dict.values()

returs alist of values

dict.items()

returns a list of dictionary in tuples 


 