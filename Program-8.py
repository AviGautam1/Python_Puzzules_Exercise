# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.

import re

def check(str):
    merged = re.split(r'([ ,]+)', str)      # An ‘r’ before a string tells the Python interpreter to treat backslashes as a literal (raw) character. Normally, Python uses backslashes as escape characters.
    return [merged[::2], merged[1::2]]


s = input("Enter A String : ")
print("Original String : ", s)
print("Split the said string into 2 lists: words and separators :", check(s))


'''
output = 
Enter A String : Hi Avinesh Gautam
Original String :  Hi Avinesh Gautam
Split the said string into 2 lists: words and separators : [['Hi', 'Avinesh', 'Gautam'], [' ', ' ']]
'''