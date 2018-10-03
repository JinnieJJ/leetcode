class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        minIdx = collections.defaultdict(int)
        ans = []
        size = len(temperatures)
        for x in range(size - 1, -1, -1):
            n = temperatures[x]
            minIdx[n] = x
            z = 0
            for y in range(n + 1, 101):
                if minIdx[y] and (minIdx[y] < z or not z):
                    z = minIdx[y]
            ans.append(z - x if z else 0)
        return ans[::-1]
        
