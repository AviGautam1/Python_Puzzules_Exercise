# Write a Python program to create string consisting of the non-negative integers up to n inclusive.


def check(num):
    return " ".join(map(str, range(num + 1)))


num = 7
print("Non-negative integer:", num)
print("Non-negative integers up to n inclusive:", check(num))


'''
output = 
Non-negative integer: 7
Non-negative integers up to n inclusive: 0 1 2 3 4 5 6 7
'''