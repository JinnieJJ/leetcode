class Solution(object):
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
        
        while left <= right and top <= bottom:
            for j in range(left, right+1):
                result.append(matrix[top][j])
            for i in range(top+1, bottom):
                result.append(matrix[i][right])
            for j in reversed(range(left, right+1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top+1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return result
