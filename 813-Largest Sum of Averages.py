class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        N = len(A)
        P = [0.0 for _ in range(N+1)]
        for i in range(N):
            P[i+1] = P[i] + A[i]
        
        dp = [0 for _ in range(N)]
        for i in range(N):
            dp[i] = (P[N] - P[i]) / (N - i)
        
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], dp[j] + (P[j] - P[i]) / (j - i))
        return dp[0]
