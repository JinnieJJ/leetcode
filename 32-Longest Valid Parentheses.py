class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        stack = []
        dp = [0] * len(s)
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                dp[i] = 0
            else:
                if len(stack) == 0:
                    dp[i] = 0
                else:
                    pos = stack.pop()
                    dp[i] = dp[pos-1] + i - pos +  1
        return max(dp)
