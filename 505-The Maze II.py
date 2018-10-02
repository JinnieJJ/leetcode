import collections
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze:
            return -1
        start, destination = tuple(start), tuple(destination)
        m, n = len(maze), len(maze[0])
        visited = {start: 0}
        q = collections.deque([(0, start[0], start[1])])
        while q:
            d, x, y = q.popleft()
            for dx, dy in [(0,1),(-1,0),(0,-1),(1,0)]:
                nx, ny, nd = x, y, d
                while 0 <= nx+dx < m and 0 <= ny+dy < n and maze[nx+dx][ny+dy] == 0:
                    nx += dx
                    ny += dy
                    nd += 1
                if (nx, ny) not in visited or visited[(nx, ny)] > nd:
                    visited[(nx, ny)] = nd
                    if (nx, ny) != destination:
                        q.append((nd, nx, ny))
        return visited.get(destination, -1)
