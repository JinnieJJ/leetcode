class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int(left+(right-left)/2)
            if nums[mid] >= target:
                right = mid
            else: 
                left = mid + 1
        if nums[left] != target:
            return [-1,-1]
        idx1 = left
        
        right = len(nums)
        while left < right:
            mid = int(left+(right-left)/2)
            if nums[mid] > target:
                right = mid
            else: 
                left = mid + 1
        idx2 = right - 1
        return [idx1, idx2]
            
