class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y + x, x + y)) # nums.sort(cmp=lambda x, y: int(y+x) - int(x+y))
        largest = ''.join(nums)
        return largest.lstrip('0') or '0'
