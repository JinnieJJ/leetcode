class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        w = len(board)
        h = len(board[0])
        
        def countBoard(x, y):
            count = 0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and board[nx][ny] == 'M':
                        count += 1
            return str(count) if count > 0 else 'B'
        
        cx, cy = click
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
            return board
        
        board[cx][cy] = countBoard(cx, cy)
        if board[cx][cy] != 'B':
            return board
        
        q = [click]
        while q:
            tx, ty = q.pop(0)
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = tx + dx, ty + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        if board[nx][ny] == 'E':
                            board[nx][ny] = countBoard(nx, ny)
                            if board[nx][ny] == 'B':
                                q.append((nx, ny))
        return board
