class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        if k == 1:
            return [[i + 1] for i in range(n)]
        if k == n:
            return [[(i + 1) for i in range(n)]]
        return [r + [n] for r in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
