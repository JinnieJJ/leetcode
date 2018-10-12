from collections import deque
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dl = deque([(float('inf'), '#')])
        for idx, l in enumerate(s):
            if l == ')':
                if dl[0][1] == '(': 
                    dl.popleft()
                elif dl[-1][1] == '*': 
                    dl.pop()
                else: return False
            else:
                if l == '(': 
                    dl.appendleft((idx, l))
                elif l == '*': 
                    dl.append((idx, l))
        while dl[-1][1] != '#' and dl[0][0] < dl[-1][0]: 
            dl.pop() 
            dl.popleft()
        return dl[0][1] == '#'
