class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l1, l2 = len(s), len(t)
        dp = [[1 for _ in range(l2+1)] for _ in range(l1+1)]
        for j in range(1, l2+1):
            dp[0][j] = 0
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * (s[i-1] == t[j-1])
        return dp[l1][l2]
