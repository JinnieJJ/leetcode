class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not start or not destination:
            return False
        visited = set()
        q = [tuple(start)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            x, y = q.pop()
            if (x, y) == tuple(destination):
                return True
            if (x, y) not in visited and maze[x][y] != 1:
                visited.add((x, y))
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
                        nx += dx 
                        ny += dy
                    q.append((nx-dx, ny-dy))
                
        
        return False
