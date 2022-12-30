# Write a Python program to check whether the given strings are palindromes or not. Return True, False.


# Palindromes are the group of words that read the same, forward and backward. E.g. “madam”
# For negative indexing, to display the 1st element to last element in steps of 1 in reverse order, we use the [::-1]. The [::-1] reverses the order.
def check(str):
    for i in str:
        if i == i[::-1]:
            return True

        else:
            return False


str = ["madam", "avi"]
print("Before Checking Palindromes In Gioven String : ", str)
print("After Checking Palindromes In Gioven String : ", check(str))


'''
output = 
Before Checking Palindromes In Gioven String :  ['madam', 'avi']
After Checking Palindromes In Gioven String :  True
'''