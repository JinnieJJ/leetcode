class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board:
            return -1
        step = 0
        board = tuple(map(tuple, board))
        q = [board]
        visited = set(board)
        while q:
            q0 =[]
            for b in q:
                if b == ((1,2,3),(4,5,0)): return step
                for x in range(2):
                    for y in range(3):
                        if b[x][y]: continue
                        for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < 2 and 0 <= ny < 3:
                                nb = list(map(list, b))
                                nb[x][y], nb[nx][ny] = nb[nx][ny], nb[x][y]
                                nb = tuple(map(tuple, nb))
                                if nb not in visited:
                                    visited.add(nb)
                                    q0.append(nb)
            q = q0
            step += 1
        return -1
