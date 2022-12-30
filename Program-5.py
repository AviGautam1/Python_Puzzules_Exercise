'''
Write a Python program to check the nth-1 string
is a proper substring of nth string in a given list of strings.
'''

str = input("Enter A String : ")
sub_str = input("Enter A Substring : ")

'''
The find() method finds the first occurrence of the specified value. 
The find() method returns -1 if the value is not found.
'''

if str.find(sub_str) == -1:
    print("Not Found !")

else:
    print("Found!")


'''
output = 
Case-1
Enter A String : hi avinesh gautam
Enter A Substring : avinesh
Found!

Case-2
Enter A String : hi avinesh gautam
Enter A Substring : hello
Not Found !
'''



