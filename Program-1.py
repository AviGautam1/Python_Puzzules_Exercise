'''
Write a Python program find a list of integers with exactly two occurrences
of nineteen and at least three occurrences of five.
'''

str = [19, 19, 5, 5, 5, 5, 1, 3]

def check(str):
    if str.count(19) == 2 and str.count(5) >= 3:
        return True

    else:
        return False


print(check(str))


# output = True

