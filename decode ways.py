class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0 for _ in range(len(s))]
        dp[len(s)] = 1
        dp[len(s) - 1] = 1 if s[len(s) - 1] != '0' else 0
        for i in range(len(s)-2, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1] + dp[i+2] if int(s[i:i+2]) <= 26 else dp[i+1]
        return dp[0]
