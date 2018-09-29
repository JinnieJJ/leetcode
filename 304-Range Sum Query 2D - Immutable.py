class NumMatrix(object):

    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        self.sums = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.sums[i][j] = self.sums[i][j-1] + matrix[i-1][j-1]
        for j in range(1, n+1):
            for i in range(1, m+1):
                self.sums[i][j] += self.sums[i-1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]
