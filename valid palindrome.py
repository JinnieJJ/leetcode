class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = [c for c in s.lower() if c.isalnum()]
        return word == word[::-1]
