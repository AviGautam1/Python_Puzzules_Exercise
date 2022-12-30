'''
We are making n stone piles! The first pile has n stones.
If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones.
Each pile must more stones than the previous pile but as few as possible.
Write a Python program to find the number of stones in each pile.
'''


test = int(input("Enter Number Of Stone Piles : "))

def check(test):
    return [test + 2 * i for i in range(test)]


print("Number Of Piles :", test)
print("Number Of Piles In Each Stoone :", check(test))


'''
output =
Case-1
Enter Number Of Stone Piles : 4
Number Of Piles : 4
Number Of Piles In Each Stoone : [4, 6, 8, 10]

Case-2
Enter Number Of Stone Piles : 7
Number Of Piles : 7
Number Of Piles In Each Stoone : [7, 9, 11, 13, 15, 17, 19]
'''


