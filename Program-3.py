'''
Write a Python program that accept an integer test
whether an integer greater than 4^4 and which is 4 mod 34.
'''


def test(n):
    if n % 34 == 4 and n > 4 ** 4:
        return True

    else:
        return False

n = 922

print("Given Integer :", n)
print("After Checking Condition : ", test(n))

n = 914

print("\nGiven Integer :", n)
print("After Checking Condition : ", test(n))


'''
output = 
Given Integer : 922
After Checking Condition :  True

Given Integer : 914
After Checking Condition :  False
'''