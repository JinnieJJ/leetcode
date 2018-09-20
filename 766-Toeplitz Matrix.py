class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True

        for j in range(len(matrix[0]) - 1, -1, -1):
            if not self.helper(matrix, 0, j):
                return False
        for i in range(len(matrix) - 1, -1, -1):
            if not self.helper(matrix, i, 0):
                return False
        return True

    def helper(self, matrix, i, j):
        digit = matrix[i][j]
        while i < len(matrix) and j < len(matrix[0]):
            if matrix[i][j] != digit:
                return False
            i += 1
            j += 1
        return True
