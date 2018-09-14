class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_bin_str = [bin(num)[2:] for num in nums] #'0bxxxx'
        nums_len = [len(bin_str) for bin_str in nums_bin_str]
        max_len = max(nums_len)
        append_len = [max_len - str_len for str_len in nums_len]
        nums_bin_list = ['0'*zero_num+nums_bin_str[i] for i, zero_num in enumerate(append_len)]
        
        total_dist = 0
        for i in range(max_len):
            bit_list = [x[i] for x in nums_bin_list]
            dist = bit_list.count('1') * bit_list.count('0')
            total_dist += dist
        return total_dist
