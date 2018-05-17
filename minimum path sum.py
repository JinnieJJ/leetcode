class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ways = [[0 for _ in range(n)] for _ in range(m)]
        ways[0][0] = grid[0][0]
        for i in range(1, m):
            ways[i][0] = ways[i-1][0] + grid[i][0]
        for j in range(1, n):
            ways[0][j] = ways[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                ways[i][j] = min(ways[i-1][j], ways[i][j-1]) + grid[i][j]
        return ways[m-1][n-1]
