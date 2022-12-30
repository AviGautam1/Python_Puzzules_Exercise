# Write a Python program find the longest string of a given list of strings.

# Method-1 using loop
list1 = ["avinesh", "deepak", "atul", "ankur"]
list2 = []
dict = {}
for str in list1:
    list2.append(len(str))
    dict[str] = len(str)
print("Maximum Length Of Given String Is :", max(list2))

for key, value in dict.items():
    if(value == max(list2)):
        print("Longest String Is :", key, ":", value)


'''
output = 
Maximum Length Of Given String Is : 7
Longest String Is : avinesh : 7
'''

# Method-2 using max() + key
test_list = ["avinesh", "deepak", "atul", "ankur"]
print("The original list : " ,test_list)
res = max(test_list, key=len)

print("Maximum length string is : " + res)


'''
output = 
The original list :  ['avinesh', 'deepak', 'atul', 'ankur']
Maximum length string is : avinesh
'''
