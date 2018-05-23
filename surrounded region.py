class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        n = len(board)
        m = len(board[0])
        queue = []
        for i in range(n):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if  board[i][m-1] == 'O':
                queue.append((i, m-1))
        for j in range(1, m-1):
            if board[0][j] == 'O':
                queue.append((0, j))
            if  board[n-1][j] == 'O':
                queue.append((n-1, j))
                
        while queue:
            r, c = queue.pop(0)
            board[r][c] = 'M'
            if r - 1 >= 0 and board[r - 1][c] == 'O':
                queue.append((r - 1, c))
            if r + 1 < n and board[r + 1][c] == 'O':
                queue.append((r + 1, c))
            if c - 1 >= 0 and board[r][c - 1] == 'O':
                queue.append((r, c - 1))
            if c + 1 < m and board[r][c + 1] == 'O':
                queue.append((r, c + 1))

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
