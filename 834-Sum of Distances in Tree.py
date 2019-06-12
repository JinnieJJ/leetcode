class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        count = [1] * N
        ans = [0] * N
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)
        
        dfs(0, None)
        dfs2(0, None)
        return ans
        
        
