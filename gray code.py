class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [(i >> 1) ^ i for i in range(pow(2, n))]
        # G(N) = B(n/2) XOR B(n)
