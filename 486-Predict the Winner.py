class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        dict = {}
        def solve(nums):
            if len(nums) == 1:
                return nums[0]
            if tuple(nums) not in dict:
                dict[tuple(nums)] = max(nums[0] - solve(nums[1:]), nums[-1] - solve(nums[:-1]))
            return dict[tuple(nums)]
        
        return solve(nums)>=0
