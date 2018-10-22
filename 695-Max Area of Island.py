class UnionFind:
    def __init__(self, N):
        self.group = N                  # all disjoint
        self.parent = list(range(N))    # point to self
        self.rank = [0] * N             # approx subtree height
        self.size = [1] * N             # tree size

    def find(self, p):
        parent = self.parent
        while p != parent[p]:
            parent[p] = parent[parent[p]] # path compression
            p = parent[p]
        return p

    def union(self, p, q):
        if p == q: 
            return
        i, j = self.find(p), self.find(q)
        if i == j: 
            return
        self.group -= 1
        parent, rank, size = self.parent, self.rank, self.size
        if rank[i] > rank[j]:
            parent[j] = i
            size[i] += size[j]
        elif rank[i] < rank[j]:
            parent[i] = j
            size[j] += size[i]
        else:
            parent[i] = j
            size[j] += size[i]
            rank[j] += 1
            
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        H = len(grid)
        if H <= 0: 
            return 0
        W = len(grid[0])
        if W <= 0: 
            return 0
        
        uf = UnionFind(H*W)
        index, max_area = -1, 0
        for r in range(H):
            for c in range(W):
                index += 1
                if grid[r][c] == 1:
                    if r > 0 and grid[r-1][c] == 1:
                        uf.union(index, index-W)
                    if c > 0 and grid[r][c-1] == 1:
                        uf.union(index, index-1)
                    max_area = max(max_area, uf.size[uf.find(index)])
        return max_area
