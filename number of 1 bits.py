class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = 0x11 | (0x11 << 8)
        tmp = tmp | (tmp << 16)
        count = n & tmp
        count += (n >> 1) & tmp
        count += (n >> 2) & tmp
        count += (n >> 3) & tmp
        count += count >> 16
        tmp = 0xf | (0xf << 8)
        count = (tmp & count) + (tmp & (count >> 4))
        return ((count & 0x1f) + (count >> 8))
