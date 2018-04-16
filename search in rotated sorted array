class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = int(left + (right-left)/2)
            if nums[mid] == target:
                return mid
            elif (nums[left] <= target < nums[mid]) or (nums[mid] < nums[left] and (not nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1
        return -1
