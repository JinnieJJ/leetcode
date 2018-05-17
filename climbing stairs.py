class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current
