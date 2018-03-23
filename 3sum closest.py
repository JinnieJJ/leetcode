class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        result = float("inf")
        min_diff = float("inf")
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                diff = sorted_nums[i]+sorted_nums[j]+sorted_nums[k]-target
                if abs(diff)<min_diff:
                    min_diff = abs(diff)
                    result = sorted_nums[i]+sorted_nums[j]+sorted_nums[k]
                if diff<0:
                    j += 1
                elif diff>0:
                    k -= 1
                else:
                    return target
        return result
