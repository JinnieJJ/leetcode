class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        targetlist = []
        for i, num in enumerate(self.nums):
            if num == target:
                targetlist.append(i)
        return targetlist[random.randint(0, len(targetlist)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
