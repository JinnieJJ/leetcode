class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        n = len(s1)
        dp = [[[False for _ in range(n+1)] for _ in range(n)] for _ in range(n)]
        
        for k in range(1, n+1):
            for i in range(n-k+1):
                for j in range(n-k+1):
                    if k == 1:
                        dp[i][j][k] = (s1[i] == s2[j])
                    else:
                        for q in range(1, k):
                            if not dp[i][j][k]:
                                dp[i][j][k] = (dp[i][j][q] and dp[i+q][j+q][k-q]) or (dp[i][j+k-q][q] and dp[i+q][j][k-q])
        return dp[0][0][n]
