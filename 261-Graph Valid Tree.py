class UF:
    def __init__(self, N):
        self.group = N                  # all disjoint
        self.parent = list(range(N))    # point to self
        self.rank = [0] * N             # subtree height

    def find(self, p):
        parent = self.parent
        while p != parent[p]:
            parent[p] = parent[parent[p]] # path compression by halving
            p = parent[p]
            ## wrong: ## p = parent[p] = parent[parent[p]]
            ## right: ## parent[p] = p = parent[parent[p]]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j: return

        self.group -= 1
        parent, rank = self.parent, self.rank
        if rank[i] < rank[j]:
            parent[i] = j
        elif rank[i] > rank[j]:
            parent[j] = i
        else:
            parent[j] = i
            rank[i] += 1 

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        
        uf = UF(n)
        for i, j in edges:
            uf.union(i, j)
        return uf.group == 1

        
