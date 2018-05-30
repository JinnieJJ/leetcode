class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord('A') - 1
        n = len(s)
        result = 0
        for i in range(n):
            result += (ord(s[n - 1 - i]) - base) * pow(26, i)
        return result
