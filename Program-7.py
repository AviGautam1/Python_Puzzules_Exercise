# Write a Python program to check a given list of integers where the sum of the first i integers is i.

'''
Python provides an inbuilt function sum() which sums up the numbers in the list.
Syntax: sum(iterable, start) iterable : iterable can be anything list , tuples or dictionaries ,
but most importantly it should be numbers. start : this start is added to the sum of numbers in the iterable.
'''

def check(num):

    return all([sum(num[:i]) == i for i in range(len(num))])


num = [1, 1, 1, 1, 1, 1]
print("Original list :", num)
print("Check the said list, where the sum of the first i integers is i :", check(num))

num = [3, 4, 5]
print("\nOriginal list :", num)
print("Check the said list, where the sum of the first i integers is i :",check(num))


'''
output = 
Original list : [1, 1, 1, 1, 1, 1]
Check the said list, where the sum of the first i integers is i : True

Original list : [3, 4, 5]
Check the said list, where the sum of the first i integers is i : False
'''