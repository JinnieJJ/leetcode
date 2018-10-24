class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            s = 0
            for j in range(i):
                s += dp[j] * dp[i - 1 - j]
            dp[i] = s
        return dp[-1]
    
    # https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
