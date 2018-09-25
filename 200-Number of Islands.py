class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1': # find 1, make all its neighbors to 0
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'

        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class UnionFind(object):
    def __init__(self):
        self.count = 0
        self.parent = {}
        self.rank = {}
    
    def add(self, line, i):
        n = len(line)
        for j in range(n):
            if line[j] == '1':
                self.parent[i * n + j] = i * n + j
                self.rank[i * n + j] = 0
                self.count += 1
                
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        uf = UnionFind()
        directions = [(0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            uf.add(grid[i], i)
            for j in range(n):
                if grid[i][j] == '1':
                    for d in directions:
                        nr, nc = i + d[0], j + d[1]
                        if nr >= 0 and nc >= 0 and grid[nr][nc] == '1':
                            uf.union(nr * n + nc, i * n + j)
        return uf.count
