class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.length = len(w)
        self.cum_weights = [0] * self.length
        self.norm = 0
        for i in range(self.length):
            self.norm += w[i]
            self.cum_weights[i] = self.norm

    def bSearch(self, target):
        i = 0
        j = self.length 
        while i < j:
            mid = (i + j) / 2
            if self.cum_weights[mid] == target:
                return mid
            elif self.cum_weights[mid] < target:
                i = mid + 1
            else:
                j = mid
        return i
    
    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.uniform(0, self.norm)
        return self.bSearch(num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
