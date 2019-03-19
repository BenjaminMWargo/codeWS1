def isBalanced(s):
    #There are only two possible values for each character in the list

    list = [] #No stack datastructure in pyton, lists can be used
    for c in s:
        if c == '[':
            list.append(c)  #
        elif c == ']':
            if not list:
                return False
            else:
                list.pop()
    if not list:
        return True
    else:
        return False

print(isBalanced("[]")) #True
print(isBalanced("[]]")) #False
print(isBalanced("[[[][][]]]")) #True
print(isBalanced("[[[[]]]]]")) #False
print(isBalanced("[[]")) #False