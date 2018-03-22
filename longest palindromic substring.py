class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        matrix = [[False for i in range(n)] for i in range(n)]
        max_len = 1
        start = 0
        for i in range(n):
             matrix[i][i] = True
        for i in range(n-1):
            j = i+1
            if s[i] == s[j]:
                max_len = 2
                start = i
                matrix[i][j] = True
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i]==s[j] and matrix[i+1][j-1]:
                    matrix[i][j] = True
                    start = i
                    max_len = l
        return s[start:start+max_len]
