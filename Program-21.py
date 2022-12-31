'''
Write a Python program to compute the sum of the ASCII
values of the upper-case characters in a given string.
'''


# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# map(function, iterables)

# The ord() function returns an integer representing the Unicode character.
# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# filter(function, iterable)

strs = input("Enter A String : ")
def check(strs):
    return sum(map(ord,filter(str.isupper, strs)))


print("Original String Is : ", strs)
print("ASCII Values Of Upper Case Character In Given String IS : ", check(strs))


'''
output = 
Enter A String : AvInesh GaUtam
Original String Is :  AvInesh GaUtam
ASCII Values Of Upper Case Character In Given String IS :  294
'''