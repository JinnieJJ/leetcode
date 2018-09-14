class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if k == 0 and list(set(nums)) == [0]:
            return True
        if k == 0:
            return False
        dp = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            m = total % k
            if m not in dp:
                dp[m] = i
            elif dp[m] < i - 1:
                return True
        return False
