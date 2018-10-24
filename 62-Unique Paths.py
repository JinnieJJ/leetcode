class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):  
            dp[i][0]= 1  
        for j in range(n):  
            dp[0][j] = 1  
        for row in range(1,m):  
            for col in range(1,n):  
                dp[row][col]=dp[row-1][col]+dp[row][col-1]  
        return dp[m-1][n-1]
