class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        v = [0] * len(graph)
        def dfs(i):
            v[i] = 1
            for e in graph[i]:
                if v[e] == 0 and not dfs(e) or v[e] == 1:  
                    return False
            v[i] = 2
            return True
        
        for i in range(len(graph)):
            if v[i] == 0: 
                dfs(i)
        return [ i for i in range(len(graph)) if v[i] == 2]
