class Solution:
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        N = len(days) # cities
        K = len(days[0]) # weeks
        dp = [0] + [-1]*(N-1)
        for w in range(K):
            ndp = [x for x in dp]
            for sc in range(N):
                if dp[sc] < 0:
                    continue
                for dc in range(N):
                    if sc == dc or flights[sc][dc]:
                        ndp[dc] = max(ndp[dc], dp[sc] + days[dc][w])
            dp = ndp
        return max(dp)
