class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        p = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    p = p+4
                    if m != 0 and grid[m-1][n] == 1:
                        p = p-1
                    if m != M-1 and grid[m+1][n] == 1:
                        p = p-1
                    if n != 0 and grid[m][n-1] == 1:
                        p = p-1
                    if n != N-1 and grid[m][n+1] == 1:
                        p = p-1
        return p
