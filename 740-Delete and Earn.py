class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        # using: the value of our previous answer
        # avoid: the value of our previous answer that doesn't use the previously largest value prev
        for k in sorted(count):
            if k-1 == prev:
                avoid, using = max(avoid, using), k * count[k] + avoid
            else:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            prev = k
        return max(avoid, using)
