class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        m, n = len(grid), len(grid[0])
        empty = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        
        def dfs(start, empty):
            if not (0 <= start[0] < m and 0 <= start[1] < n and grid[start[0]][start[1]] >= 0): 
                return
            if start == end and empty == 0:
                self.res += 1
                return
            grid[start[0]][start[1]] = -2
            dfs((start[0] + 1, start[1]), empty - 1)
            dfs((start[0] - 1, start[1]), empty - 1)
            dfs((start[0], start[1] + 1), empty - 1)
            dfs((start[0], start[1] - 1), empty - 1)
            grid[start[0]][start[1]] = 0
        
        dfs(start, empty)
        return self.res
