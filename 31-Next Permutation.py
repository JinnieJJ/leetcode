class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        high = -1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                high = i
        if high == -1:
            nums.reverse()
            return

        low = -1
        for i in range(high+1, len(nums)):
            if nums[i] > nums[high]:
                low = i

        nums[high], nums[low] = nums[low], nums[high]
        nums[high+1:] = sorted(nums[high+1:])
