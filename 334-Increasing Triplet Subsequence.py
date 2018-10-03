class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        minimum, a, b = float('inf'), float('inf'), float('inf')
        for n in nums:
            if minimum >= n:
                minimum = n
            elif b >= n:
                a, b = minimum, n
            else:
                return True
        return False
