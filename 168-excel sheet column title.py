class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        base = ord('A')
        while n:
            n, r = divmod(n - 1, 26)
            result.append(chr(base + r))
        return ''.join(result[::-1])
