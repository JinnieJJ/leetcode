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
    
    # h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2)
