class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dirs = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
        
        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K+1)]
        dp[0][r][c] = 1
        for step in range(1, K+1):
            for i in range(N):
                for j in range(N):
                    for d in dirs:
                        x = i + d[0]
                        y = j + d[1]
                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue
                        dp[step][i][j] += dp[step-1][x][y] * 0.125
        res = 0.0
        for i in range(N):
            for j in range(N):
                res += dp[K][i][j]
                
        return res
