class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        n = len(nums)
        while i < n - 1:
            if i % 2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i % 2 != 0 and nums[i] < nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
            i+=1
