class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        self.bit = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        self.matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.update(i, j, matrix[i][j])
        
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        adjust = val - self.matrix[row][col]
        self.matrix[row][col] = val
        row += 1
        col += 1
        i = row
        while i <= len(self.matrix):
            j = col
            while j <= len(self.matrix[0]):
                self.bit[i][j] += adjust
                j += (j & -j)
            i += (i & -i)


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return  self.sum(row2, col2) - self.sum(row2, col1-1) - self.sum(row1-1, col2) + self.sum(row1-1, col1-1)
        
    def sum(self, row, col):
        row += 1
        col += 1
        ret = 0
        i =  row
        while i > 0:
            j = col
            while j > 0:
                ret += self.bit[i][j]
                j -= (j & -j)
            i -= (i &  -i)
        return ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
