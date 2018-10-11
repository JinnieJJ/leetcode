class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        wcount = collections.Counter(s)
        one = 0
        for c in wcount.values():
            if c % 2 == 1:
                one += 1
            if one > 1:
                return False
        return True
