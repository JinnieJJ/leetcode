class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sums = [0] * (len(A) + 1)
        for i in range(len(A)):
            sums[i+1] = sums[i] + A[i]
        
        queue = collections.deque()
        res = len(A) + 1
        for i in range(len(A) + 1):
            while queue and sums[i] - sums[queue[0]] >= K:
                res = min(res, i - queue.popleft())
            while queue and sums[i] <= sums[queue[-1]]:
                queue.pop()
            queue.append(i)
        return res if res <= len(A) else -1 
