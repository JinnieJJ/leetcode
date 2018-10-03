class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        dic1 = [0]*26
        dic2 = [0]*26
        res = []
        for i in range(len(p)):
            dic1[ord(p[i])-ord('a')] += 1
            dic2[ord(s[i])-ord('a')] += 1
        if dic1 == dic2:
            res.append(0)
        for i in range(1, len(s)-len(p)+1):
            dic2[ord(s[i-1])-ord('a')] -= 1
            dic2[ord(s[i+len(p)-1])-ord('a')] += 1
            if dic1 == dic2:
                res.append(i)
        return res
