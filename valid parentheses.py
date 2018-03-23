class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapper = {"(":")", "{":"}", "[":"]"}
        for p in s:
            if p in mapper:
                stack.append(p)
            elif len(stack)==0:
                return False
            elif mapper[stack.pop()]!=p:
                return False
        return len(stack) == 0
