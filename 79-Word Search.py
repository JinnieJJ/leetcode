class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.Recursion(board, word, 0, i, j, visited):
                    return True
        return False
        
    def Recursion(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.Recursion(board, word, cur + 1, i + 1, j, visited) or\
                 self.Recursion(board, word, cur + 1, i - 1, j, visited) or\
                 self.Recursion(board, word, cur + 1, i, j + 1, visited) or\
                 self.Recursion(board, word, cur + 1, i, j - 1, visited)
        visited[i][j] = False

        return result
