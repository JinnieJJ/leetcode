class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        result = [[1]]
        while numRows > 1:
            result.append([1] + [a + b for a, b in zip(result[-1][:-1], result[-1][1:])] + [1])
            numRows -= 1
        return result
