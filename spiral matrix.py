class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if matrix == []:
            return result
        
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        
        while left<=right and top<=bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            for j in range(top+1, bottom):
                result.append(matrix[j][right])
            for k in reversed(range(left, right+1)):
                if top < bottom:
                    result.append(matrix[bottom][k])
            for m in reversed(range(top+1, bottom)):
                if left < right:
                    result.append(matrix[m][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return result
