# Write a Python program find the strings in a given list containing a given substring.


# Method-1
string = input("Enter string : ")
sub_str = input("Enter word : ")

if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")


'''
output = 
Enter string : avinesh gautam
Enter word : avi
Substring in string!
'''


# Method-2
def test(strs, substr):
    return [s for s in strs if substr in s]


strs = ["avinesh", "ankur", "atul", "deepak"]
substr = "av"

print("\nOriginal String : ", strs)
print("Substring Is : ", test(strs, substr))


'''
output = 
Original String :  ['avinesh', 'ankur', 'atul', 'deepak']
Substring Is :  ['avinesh']
'''