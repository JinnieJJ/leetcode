class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        ans = [-1] + [i for i in range(l)]
        isPal = [[False] * (i + 1) for i in range(l)]
        for i in range(l):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPal[i - 1][j + 1]):
                    isPal[i][j] = True
                    ans[i + 1] = min(ans[i + 1], ans[j] + 1)
        return ans[l]
