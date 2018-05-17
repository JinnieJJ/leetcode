class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq = ""
        k -= 1
        fact = 1
        for i in range(1, n):
            fact *= i
        nums = [i for i in range(1, n+1)]
        for i in reversed(range(n)):
            curr = nums[int(k/fact)]
            seq += str(curr)
            nums.remove(curr)
            if i > 0:
                k = k % fact
                fact = int(fact/i)
        return seq
