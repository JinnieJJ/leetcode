class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return
        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        for i in range(1, len(self.bit)):
            self.bit[i] = nums[i-1] + self.bit[i-1]
        
        for i in range(len(self.bit)-1, 0, -1):
            last_i = i - (i & -i)
            self.bit[i] -= self.bit[last_i]


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if val - self.nums[i]:
            self.add(i, val - self.nums[i])
            self.nums[i] = val
            
    def add(self, i, val):
        i += 1
        while i <= len(self.nums):
            self.bit[i] += val
            i += (i & -i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i-1)
    
    def sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= (i & -i)
        return ret
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
