class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive, negative = nums[0], nums[0]
        result = nums[0]
        for num in nums[1:]:
            # Keep the largest and smallest product
            positive, negative = max(num, positive * num, negative * num), min(num, positive * num, negative * num)
            result = max(result, positive)
        return result
