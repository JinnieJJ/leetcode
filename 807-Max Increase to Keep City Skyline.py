class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rows[i], cols[j]) - grid[i][j]
        return res
        
