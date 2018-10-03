class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        lenS, lenT = len(S), len(T)
        start = -1
        minLen = float('inf')
        dp = [[-1 for _ in range(lenT+1)] for _ in range(lenS+1)]
        for i in range(lenS+1):
            dp[i][0] = i
        for i in range(1, lenS+1):
            for j in range(1, min(i, lenT)+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
            if dp[i][lenT] != -1:
                length = i - dp[i][lenT]
                if minLen > length:
                    minLen = length
                    start = dp[i][lenT]
                
        return S[start:start+minLen] if start != -1 else ""
