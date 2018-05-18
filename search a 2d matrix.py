class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if not matrix or not matrix[0]:
        #     return False
        # row = 0
        # while row < len(matrix) and matrix[row][0] <= target:
        #     row += 1
        # row -= 1
        # column = 0
        # while column < len(matrix[0]) and matrix[row][column] <= target:
        #     column += 1
        # column -= 1
        # if matrix[row][column] == target:
        #     return True
        # return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = left + int((right - left) / 2)
            if matrix[int(mid/n)][mid % n] >= target:
                right = mid
            else:
                left = mid + 1

        return left < m*n and matrix[int(left/n)][left%n] == target
