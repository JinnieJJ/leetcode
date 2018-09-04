class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
    
    def reverseWords2(self, s):
        s = s.split(" ")
        if len(s) == 0:
            return ""
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        res = []
        for i in range(len(s)):
            if s[i] != "":
                res.append(s[i])
        return " ".join(res)
