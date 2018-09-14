class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] == S:
            return 1
        
        dp = [collections.defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for key, count in dp[i].items():
                dp[i+1][key + num] += count
                dp[i+1][key - num] += count
        return dp[len(nums)][S]
