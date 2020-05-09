class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = [False] * len(nums)
        self.Recursion(result, used, [], sorted(nums))
        return result

    def Recursion(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur[:])
            return
        for i in range(len(nums)):
            if used[i] or (i>0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            cur.append(nums[i])
            self.Recursion(result, used, cur, nums)
            cur.pop()
            used[i] = False
        
