'''
Write a Python program to check the nth-1 string
is a proper substring of nth string in a given list of strings.
'''

str = input("Enter A String : ")
sub_str = input("Enter A Substring : ")

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



