'''
Write a Python program to split a given string (s) into strings if there is a space in the string,
otherwise split on commas if there is a comma, otherwise return the list of lowercase letters
with odd order (order of a = 0, b = 1, etc.)
'''


def check(str):
    if " " in str:
        return str.split(" ")

    if " ," in str:
        return str.split(" ,")

    return [c for c in str if c.islower() and ord(c) % 2 == 0]      # The ord() function returns an integer representing the Unicode character.


str = "a v i n e s h"
print("Original string : ", str)
print("After Split The String : ", check(str))

str = "a, v, i, n, e, s, h"
print("\nOriginal string : ", str)
print("After Split The String : ", check(str))

str = "avinesh"
print("\nOriginal string : ", str)
print("After Split The String : ", check(str))


'''
output = 
Original string :  a v i n e s h
After Split The String :  ['a', 'v', 'i', 'n', 'e', 's', 'h']

Original string :  a, v, i, n, e, s, h
After Split The String :  ['a,', 'v,', 'i,', 'n,', 'e,', 's,', 'h']

Original string :  avinesh
After Split The String :  ['v', 'n', 'h']
'''