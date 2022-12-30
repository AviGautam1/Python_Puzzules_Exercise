# Write a Python program to find the indexes of numbers of a given list below a given threshold.



def check(nums, limit):

    return [i for i, n in enumerate(nums) if n < limit]


nums = [1, 3, 5, 44, 55, 80, 444, 676, 2, 1]
limit = 50

print("Before Checking Threshold : ", nums)
print("Check the indexes of numbers of the said list below the given threshold:", check(nums, limit))


'''
output = 
Before Checking Threshold :  [1, 3, 5, 44, 55, 80, 444, 676, 2, 1]
Check the indexes of numbers of the said list below the given threshold: [0, 1, 2, 3, 8, 9]
'''

