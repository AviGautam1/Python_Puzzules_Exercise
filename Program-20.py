'''
Write a Python program to check, for each string in a given list, whether the last character is an
isolated letter or not. Return True or False.
'''


def check(str):
    for s in str:
        if len(s.split(" ")[-1]) == 1:
            return "Isolated Letter Present True"

        else:
            return "Not Isolated Letter Not Present False"


str = ["av i", "atul"]
print("Original String : ", str)
print("After Checking Condition : ", check(str))

str = ["avi", "atul"]
print("\nOriginal String : ", str)
print("After Checking Condition : ", check(str))


'''
output = 
Original String :  ['av i', 'atul']
After Checking Condition :  Isolated Letter Present True

Original String :  ['avi', 'atul']
After Checking Condition :  Not Isolated Letter Not Present False
'''

