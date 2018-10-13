class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum_cur = start = 0
        min_length = float('inf')
        
        for cur, num in enumerate(nums):
		    sum_cur += num
            
		    if sum_cur >= s:

			    while sum_cur >= s:
				    sum_cur -= nums[start]
				    start += 1

			    min_length = min(min_length, (cur - start + 2))
                
        return min_length if min_length < float('inf') else 0
