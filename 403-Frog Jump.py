class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        memo = {}
        idx = {stones[i]:i for i in range(len(stones))}
        
        def dp(i, p):
            if i >= len(stones) - 1: 
                return i == len(stones) - 1
            if (i, p) not in memo: # not visited
                memo[(i, p)] = any(dp(idx[stones[i] + k], k) for k in (p - 1, p, p + 1) if k > 0 and stones[i] + k in idx and idx[stones[i] + k] > i)
            return memo[(i, p)]
        return dp(0, 0)
