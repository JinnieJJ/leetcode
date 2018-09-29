class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        down = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        right = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if grid[i][j] != 'W':
                    if i + 1 < len(grid):
                        down[i][j] = down[i+1][j]
                    if j + 1 < len(grid[0]):
                        right[i][j] = right[i][j+1]
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                        right[i][j] += 1
        
        up = [0 for _ in range(len(grid[0]))]
        result = 0

        for i in range(len(grid)):
            left = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'W':
                    left = 0
                    up[j] = 0
                elif grid[i][j] == 'E':
                    left += 1
                    up[j] += 1
                else:
                    result = max(result, down[i][j] + right[i][j] + left + up[j])
        return result
