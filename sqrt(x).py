class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1

        left, right = 1, int(x/2)
        while left <= right:
            mid = left + int((right - left)/2)
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
                
        return left - 1
