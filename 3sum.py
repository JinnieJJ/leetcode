class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        solutions = set()
        unique_set = set(nums)
        
        if len(unique_set) == 1 and 0 in unique_set and len(nums) > 2:
            return [[0, 0, 0]]

        i = 0
        for i in range(n-2):
            num = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                s = num + left_num + right_num
                if s == 0:
                    solutions.add(tuple([right_num, num, left_num]))
                    right -= 1
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1

        return list(solutions)
