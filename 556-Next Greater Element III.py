class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = [int(x) for x in str(n)]
        i = len(n) - 1
        while i > 0 and n[i-1] >= n[i]:
            i -= 1
        if i == 0:
            return -1
        idx_bigger = i-1
        while i+1 < len(n) and n[i+1] > n[idx_bigger]:
            i += 1
        n[i], n[idx_bigger] = n[idx_bigger], n[i]
        n = n[:idx_bigger+1] + sorted(n[idx_bigger+1:])
        ans = int(''.join([str(x) for x in n]))
        if ans > 2 << 31 - 1:
            return -1
        else:
            return ans
