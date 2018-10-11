class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)
        
    def helper(self, n, k):
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        if k == 0:
            return ['']
        elif k == 1:
            return ['0', '1', '8']
        result = []
        for num in self.helper(n, k-2):
            for key, val in lookup.items():
                if n == k and key == '0':
                    continue
                result.append(key + num + val)
        return result
                    
