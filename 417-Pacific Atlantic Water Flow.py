class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: 
            return []
        m, n = len(matrix), len(matrix[0])
        
        def bfs(reachable_ocean):
            q = collections.deque(reachable_ocean)
            while q:
                (i, j) = q.popleft()
                for (di, dj) in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= di+i < m and 0 <= dj+j < n and (di+i, dj+j) not in reachable_ocean \
                        and matrix[di+i][dj+j] >= matrix[i][j]:
                        q.append((di+i,dj+j))
                        reachable_ocean.add((di+i, dj+j))
            return reachable_ocean 
        
        pacific = set ([(i, 0) for i in range(m)] + [(0, j) for j  in range(1, n)]) 
        atlantic = set ([ (i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)]) 
        return list(bfs(pacific) & bfs(atlantic))
