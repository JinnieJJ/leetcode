class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    islands.add(self.bfs(grid, x, y))
        return len(islands)

    def bfs(self, grid, x, y):
        w, h = len(grid), len(grid[0])
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        queue = [(x, y)]
        grid[x][y] = 0
        ans = []
        while queue:
            x, y = queue.pop(0)
            ans.append((x, y))
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    if grid[nx][ny]:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
        top = min(x for x, y in ans)
        left = min(y for x, y in ans)
        return tuple((x - top) * h + y - left for x,  y in sorted(ans))
