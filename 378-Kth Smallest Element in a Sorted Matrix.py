class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        i = matrix[0][0]
        j = matrix[m-1][n-1]
        res = 0
        while i <= j:
            mid = i + (j - i) // 2
            if self.before(matrix, k, mid):
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res
    
    
    def before(self, matrix, k, t):
        count = 0
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= t:
                i += 1
                count += j + 1
                if count >= k:
                    return True
            else:
                j -= 1
        return False
