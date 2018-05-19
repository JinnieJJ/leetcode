class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        previous_size = 0
        for i in range(len(nums)):
            current_size = len(result)
            # print previous_size, current_size
            for j in range(current_size):
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    result.append(list(result[j]))
                    # print result
                    result[-1].append(nums[i])
                    # print result
            previous_size = current_size
        return result
