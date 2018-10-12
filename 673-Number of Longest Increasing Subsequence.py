class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxLength = maxCount = 0
        size = len(nums)
        dp = [1] * size # 表示以x结尾的子序列中最长子序列的长度
        dz = [1] * size # 表示以x结尾的子序列中最长子序列的个数
        for x in range(size):
            for y in range(0, x):
                if nums[x] > nums[y]:
                    if dp[y] + 1 > dp[x]:
                        dp[x] = dp[y] + 1
                        dz[x] = dz[y]
                    elif dp[y] + 1 == dp[x]:
                        dz[x] += dz[y]
        maxLength = max(max(dp), 0)
        ans = 0
        for p, z in zip(dp, dz):
            if p == maxLength:
                ans += z
        return ans
