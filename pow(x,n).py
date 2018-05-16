class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0 :
            return 1.0/self.myPow(x, -n)
        if n == 0:
            return 1
        v = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return v*v
        else:
            return v*v*x
