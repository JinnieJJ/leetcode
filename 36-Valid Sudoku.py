class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            line = list(filter(lambda x: x != ".", [board[i][j] for j in range(9)]))
            column = list(filter(lambda x: x != ".", [board[j][i] for j in range(9)]))
            if len(set(line)) != len(line) or len(set(column)) != len(column):
                return False

        for i in range(3):
            for j in range(3):
                square = list(filter(lambda x: x != ".", [board[m][n] for n in range(3*j, 3*j+3) for m in range(3*i, 3*i+3)]))
                if len(set(square)) != len(square):
                    return False
        return True
