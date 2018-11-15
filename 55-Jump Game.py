class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i, step in enumerate(nums):
            if i > count:
                break
            count = max(count, i + step)
        return count >= len(nums) - 1
