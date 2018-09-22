import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """ 
        adj = collections.defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        
        best = collections.defaultdict(lambda: collections.defaultdict(lambda: float('Inf')))
        min_heap = [(0, src, K+1)]
        while min_heap:
            result, c, k = heapq.heappop(min_heap)
            if https://leetcode.com/submissions/detail/177642651/k < 0 or best[c][k] < result:
                continue
            if c == dst:
                return result
            for nc, p in adj[c]:
                if result + p < best[nc][k-1]:
                    best[nc][k-1] = result + p
                    heapq.heappush(min_heap, (result+p, nc, k-1))
        return -1
