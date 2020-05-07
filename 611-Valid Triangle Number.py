class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums)-1):
                master = nums[i] + nums[j]
                left = j + 1
                right = len(nums) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < master:
                        left = mid + 1
                    else:
                        right = mid - 1
                count += (right - j)
        return count
