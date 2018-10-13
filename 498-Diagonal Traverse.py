from collections import deque, defaultdict
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        
        m, n = len(matrix), len(matrix[0])
        result = defaultdict(deque)
        for i in range(m):
            for j in range(n):
                s = i + j
                if s & 1:
                    result[s].append(matrix[i][j])
                else:
                    result[s].appendleft(matrix[i][j])
        output = []
        for s in range(m + n - 1):
            output.extend(result[s])
        return output
