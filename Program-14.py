# Write a Python program to find the lengths of a given list of non-empty strings.


def check(str):
    return [*map(len, str)]         # map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)


str = ["avi", "deepak", "atul", ""]
print("Original strings :", str)
print("Length Of String Include Non Emty String :", check(str))


'''
output = 
Original strings : ['avi', 'deepak', 'atul', '']
Length Of String Include Non Emty String : [3, 6, 4, 0]
'''