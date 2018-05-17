class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            for j in range(top + 1, bottom):
                matrix[j][right] = num
                num += 1
            for m in reversed(range(left, right + 1)):
                if top < bottom:
                    matrix[bottom][m] = num
                    num += 1
            for k in reversed(range(top + 1, bottom)):
                if left < right:
                    matrix[k][left] = num
                    num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return matrix
