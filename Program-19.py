'''
Monotonic sequences are sequences, which constantly increase or constantly decrease.
Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
'''


def check(num):
    for i in range(len(num) - 1):
        if num[i] < num[i+1]:
            return "Increasing Monotonic Sequence"

        if num[i+1] < num[i]:
            return "Decreasing Monotonic Sequence"

        else:
            return "Not Monotonic Sequence"


num = [1, 2, 4, 6, 8]
print("Original Sequence : ", num)
print("After Checking Sequence : ", check(num))

num = [12, 8, 6, 4, 2]
print("\nOriginal Sequence : ", num)
print("After Checking Sequence : ", check(num))

num = [19,19,5,5,5,5,5]
print("\nOriginal Sequence : ", num)
print("After Checking Sequence : ", check(num))


'''
output = 
Original Sequence :  [1, 2, 4, 6, 8]
After Checking Sequence :  Increasing Monotonic Sequence

Original Sequence :  [12, 8, 6, 4, 2]
After Checking Sequence :  Decreasing Monotonic Sequence

Original Sequence :  [19, 19, 5, 5, 5, 5, 5]
After Checking Sequence :  Not Monotonic Sequence
'''