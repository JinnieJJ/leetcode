class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        memory = [[None]*len(matrix[0]) for i in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res,self.helper(i, j, matrix, memory))
        return res
    
    def helper(self,i,j,matrix,memory):
        if memory[i][j]:
            return memory[i][j]
        count = 0
        if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
            count = max(count,self.helper(i-1, j, matrix, memory))
        if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
            count = max(count,self.helper(i, j-1, matrix, memory))
        if i+1 < len(matrix) and matrix[i+1][j] > matrix[i][j]:
            count = max(count,self.helper(i+1, j, matrix, memory))
        if j+1 < len(matrix[0]) and matrix[i][j+1] > matrix[i][j]:
            count = max(count,self.helper(i, j+1, matrix, memory))    
        memory[i][j] = count + 1
        return count + 1
