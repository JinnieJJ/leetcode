class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) >= len(t):
            i = 0
            while i < len(t) and s[i] == t[i]:
                i += 1
            if s != t:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
            else:
                return False
        else:
            return self.isOneEditDistance(t, s)
