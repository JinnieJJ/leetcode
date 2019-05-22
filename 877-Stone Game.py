class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        # dp[i+1][j+1] = the value of the game [piles[i], ..., piles[j]].
        for size in range(1, n+1):
            for i in range(n-size+1):
                j = i + size - 1
                if (i + j + n) % 2 == 1:
                    dp[i+1][j+1] = max(piles[i]+dp[i+2][j+1], piles[j]+dp[i+1][j])
                else:
                    dp[i+1][j+1] = min(dp[i+2][j+1]-piles[i], dp[i+1][j]-piles[j])
        return dp[1][n] > 0
