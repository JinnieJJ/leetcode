class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        candidate = [] # find node with degree 2 (2 parents)
        self.par = [0] * (len(edges)+1)
        for u,v in edges:
            if self.par[v] != 0:
                candidate.append([self.par[v], v])
                candidate.append([u,v])
                break
            else:
                self.par[v] = u
        
        self.par = range(len(edges)+1)
        for u,v in edges:
            if candidate and [u,v] == candidate[1]:
                continue
            if self.unionFind(u) == v:
                # there is cycle
                if candidate:
                    # return the edge that forms the cycle and also points to node with degree 2
                    return candidate[0] 
                # no node with degree 2, return the last edge that forms the cycle
                return [u,v]
            self.par[v] = u
        return candidate[1]
    
    def unionFind(self, u):
        if self.par[u] != u:
            self.par[u] = self.unionFind(self.par[u])
        return self.par[u]
