# Binary Search
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        r = []
        for env in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            pos = bisect.bisect_left(r, env[1])
            if pos == len(r):
                r.append(env[1])
            elif env[1] < r[pos]:
                r[pos] = env[1]
        return len(r)
        
# DP (TLE)
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: x[0])
        n = len(envelopes)
        dp = [1] * n
        maxans = 1
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxans = max(maxans, dp[i])
        return maxans
