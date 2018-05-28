class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for num in nums:
            # calculate the count of the each bit
            three = two & num
            two = two | one & num
            one = one | num
            # clear the count for the bit which has achieved three
            one = one & ~three
            two = two & ~three
        return one
