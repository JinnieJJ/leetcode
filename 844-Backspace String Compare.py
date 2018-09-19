class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        t = []
        for c in S:
            if c != '#':
                s.append(c)
            elif c == '#' and s != []:
                s.pop()
        for c in T:
            if c != '#':
                t.append(c)
            elif c == '#' and t != []:
                t.pop()
        if "".join(s) == "".join(t):
            return True
        return False
            
