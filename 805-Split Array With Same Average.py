class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort(reverse = True)
        dp = {0 : 0}
        size, total = len(A), sum(A)
        for a in A:
            for k in sorted(dp.keys(), reverse = True):
                dp[k + a] = dp[k] + 1
                k += a
                v = dp[k]
                if v and size - v and k * (size - v) == (total - k) * v:
                    return True
        return False
