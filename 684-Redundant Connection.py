class UnionFind(object):
    def __init__(self, edges):
        self.parents = {}
        for e in edges:
            self.parents[e[0]] = e[0]
            self.parents[e[1]] = e[1]
    
    def find(self, v):
        if self.parents[v] != v:
            self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 != p2:
            self.parents[v1] = p2
            self.parents[p1] = p2


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        u = UnionFind(edges)
        for e in edges:
            p1 = u.find(e[0])
            p2 = u.find(e[1])
            if p1 != p2:
                u.union(e[0], e[1])
            else:
                return e
