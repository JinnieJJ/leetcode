class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dict[stack.pop()] = n
            stack.append(n)
        return [dict.get(n, -1) for n in findNums]
