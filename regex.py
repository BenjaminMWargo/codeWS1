import re
#https://regexr.com - Regular expression calculator
def isValidPhoneNumber(s):
    #A valid phone number is formatted (###)###-#### 
    return re.match("(\(\d{3}\)\d{3}-\d{4})\Z",s)

#Regular Expressions are used to find patterns in strings
#re.match compares a regular expression to a string
# () are a capture group, used to group sections together
#\ is an escape, this will either take the next character literally or use its alternative definition
# ( normally means capture group but \( is the literally character "("
# d noramlyl means the literal character "d" but \d represents at digit
# {3} is a quanitifier, it means exactly 3 copies of whatever was before it. In this case, digits
# \Z means end of string. If you don't have this, a string that matches in its first half but has more characters after would match

print(isValidPhoneNumber("(814)269-7000")) #True, all else false
print(isValidPhoneNumber("8142697000"))
print(isValidPhoneNumber("(814)-269-7000"))
print(isValidPhoneNumber("((814))269-7000"))
print(isValidPhoneNumber("(814)269-70004")) # if there wasn't a /Z in the regex, then this would match
print(isValidPhoneNumber("(814)2269-7000"))
print(isValidPhoneNumber("(8142)269-7000"))