class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if not s and not t:
            return True
        
        length = len(s)
        dicts = {}
        dictt = {}
        for i in range(length):
            if s[i] in dicts:
                if t[i] != dicts[s[i]]:
                    return False
            else:
                if t[i] in dictt:
                    return False
                dicts[s[i]] = t[i]
                dictt[t[i]] = s[i]
        return True
