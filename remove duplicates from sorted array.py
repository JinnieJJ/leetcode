class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = list(set(nums))
        # return len(nums)
        
        # cannot use set()
        # it has to copy the elements one by one
        # the problem does not allow any extra storage array
        
        if not nums:
            return 0
        
        i, j = 1, 0
        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            i += 1
            
        return j + 1
