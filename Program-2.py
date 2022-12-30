'''
Write a Python program that accept a list of integers and check the length
and the fifth element. Return true if the length of the list is 8 and fifth
element occurs thrice in the said list.
'''


lst1 = ['2', '3', '7', '3', '1', '7', '7', '12', '13']
#lst2 = ['2', '3', '5', '3', '1', '7', '8']
print("Original List :", lst1)

def check(lst1):
    if len(lst1) >= 8 and lst1.count(lst1[5]) == 3:
        return True

    else:
        return False


print("After Checking Condition :", check(lst1))


'''
output = True
Original List : ['2', '3', '7', '3', '1', '7', '7', '12', '13']
After Checking Condition : True
'''