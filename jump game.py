class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        
        for i,x in enumerate(nums):
            if i > count:
                break
            count = max(count, i+x)
        return count >= len(nums) - 1
