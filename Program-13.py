# Write a Python program to find the strings in a given list, starting with a given prefix.


def check(str, prefix):
    return [s for s in str if s.startswith(prefix)]
    '''
    for s in str:
        if s.startswith(prefix):
            return True

        else:
            return False
    '''


str = ["avi", "atul", "deepak", "ankur"]
prefix = "a"
print("Before Checking Prefix a In The Given String :", str)
print("Before Checking Prefix a In The Given String :", check(str, prefix))


'''
output = 
Before Checking Prefix a In The Given String : ['avi', 'atul', 'deepak', 'ankur']
Before Checking Prefix a In The Given String : ['avi', 'atul', 'ankur']
'''