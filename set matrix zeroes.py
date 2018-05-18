class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = [False for _ in range(m)]
        columns = [False for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    columns[j] = True
        
        for i in range(m):
            for j in range(n):
                if rows[i] == True or columns[j] == True:
                    matrix[i][j] = 0
        
