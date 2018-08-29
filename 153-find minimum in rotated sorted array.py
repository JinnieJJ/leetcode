class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)
        target = nums[-1]

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1

        return nums[left]
