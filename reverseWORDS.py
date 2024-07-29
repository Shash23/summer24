def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    stack = []

    s = s.strip()
    s = s.split()

    for i in s:

        if i == '' and stack[-1] == '':
            continue
        
        else:
            stack.append(i)
            
    result = ''

    amt = len(stack)
    
    #print(stack)
    
    
    for j in range(amt):
        result += stack.pop()
        result += " "
        print(result)
        
    result = result.strip()
    print(result)
    
    return result
        
print(reverseWords("the sky is blue"))

'''
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
'''