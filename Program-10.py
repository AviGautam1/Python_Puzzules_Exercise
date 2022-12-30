'''
Given a string consisting of whitespace and groups of matched parentheses,
write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
'''


def match_parentheses(test):

   lst = []
   s1 = ""
   for s2 in test.replace(" ", ""):
       s1 += s2      # s1 = s1 + s2
       if s1.count("(") == s1.count(")"):
           lst.append(s1)
           s1 = ""
   return lst


test = "() (( ( )() (  )) ) ( ())"
print("Before Matching Parentheses : ", test)
print("After Matching Parentheses : ",match_parentheses(test))


'''
output = 
Before Matching Parentheses :  () (( ( )() (  )) ) ( ())
After Matching Parentheses :  ['()', '((()()()))', '(())']
'''