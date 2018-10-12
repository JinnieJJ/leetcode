import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = collections.Counter(nums)
        ans = [x for x,y in c.most_common(k)]
        return ans
