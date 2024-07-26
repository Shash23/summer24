class Solution(object):
    def reverseWords(self, s):
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

        for j in range(amt):
            result += stack.pop()


        return result
        