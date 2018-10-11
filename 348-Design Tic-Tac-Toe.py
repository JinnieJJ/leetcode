class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diagonal = [0, 0]
        self.antidiagonal = [0, 0]
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        i = player - 1
        self.rows[row][i] += 1
        self.cols[col][i] += 1
        if row == col:
            self.diagonal[i] += 1
        if row == self.n - 1 - col:
            self.antidiagonal[i] += 1
        if self.rows[row][i] == self.n or self.cols[col][i] == self.n or self.diagonal[i] == self.n or self.antidiagonal[i] == self.n:
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
