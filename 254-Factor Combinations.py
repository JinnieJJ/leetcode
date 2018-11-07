class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return []
        res = []
        def dfs(path, rest, target):
            if len(path) > 0:
                res.append(path + [target])
            for i in range(rest, int(math.sqrt(target)) + 1): # i <= target//i, i.e., i <= sqrt(target)
                if target % i == 0:
                    dfs(path + [i], i, target//i)
        dfs([], 2, n)
        return res
