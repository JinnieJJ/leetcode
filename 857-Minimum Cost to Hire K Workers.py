import heapq
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        
        workers = sorted([wage[i]/quality[i], quality[i]] for i in range(len(quality)))
        res = float('inf')
        qsum = 0
        heap = []
        
        for i in range(len(workers)):
            r, q = workers[i]
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                # 始终丢弃quality最大的人
                qsum += heapq.heappop(heap) # return the smallest value from the heap
            if len(heap) == K:
                res = min(res, qsum * r)
        return res
