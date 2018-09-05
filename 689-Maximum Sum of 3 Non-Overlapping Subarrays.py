class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        W = [] # sums of windows
        wsum = 0
        for i, x in enumerate(nums): # calculate sum of each K-element subarray
            wsum += x
            if i >= K: 
                wsum -= nums[i-K]
            if i >= K-1:
                W.append(wsum)

        left = [0] * len(W) # track the best left index
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W) # track the best right index
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None # get the sum
        for j in range(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
