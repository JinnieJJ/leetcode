class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        # dp[i]: the probability of getting points i
        if K == 0 or N >= K + W:
            return 1
        dp = [0.0 for _ in range(N + 1)]
        dp[0] = 1
        Wsum = 1.0
        # Wsum表示（前W个dp之和）/ W，相当于维护一个sliding window
        for i in range(1, N+1):
            dp[i] = Wsum / W
            if i < K:
                Wsum += dp[i]
            # 因为只需要计算前w个dp之和，所以当i>=W时，减去最前面的dp。
            if 0 <= i - W < K: 
                Wsum -= dp[i - W]
        return sum(dp[K:])
