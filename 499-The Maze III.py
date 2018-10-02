class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        ball, hole = tuple(ball), tuple(hole)
        dmap = collections.defaultdict(lambda: collections.defaultdict(int))
        w, h = len(maze), len(maze[0])
        for dir in 'dlru': dmap[hole][dir] = hole
        for x in range(w):
            for y in range(h):
                if maze[x][y] or (x, y) == hole: continue
                if x > 0 and dmap[(x - 1, y)]['u']:
                    dmap[(x, y)]['u'] = dmap[(x - 1, y)]['u']  
                else:
                    dmap[(x, y)]['u'] = (x, y)
                if y > 0 and dmap[(x, y - 1)]['l']:
                    dmap[(x, y)]['l'] = dmap[(x, y - 1)]['l']  
                else:
                    dmap[(x, y)]['l'] = (x, y)
        for x in range(w - 1, -1, -1):
            for y in range(h - 1, -1, -1):
                if maze[x][y] or (x, y) == hole: continue
                if x < w - 1 and dmap[(x + 1, y)]['d']: 
                    dmap[(x, y)]['d'] = dmap[(x + 1, y)]['d']
                else: 
                    dmap[(x, y)]['d'] = (x, y)
                if y < h - 1 and dmap[(x, y + 1)]['r']:
                    dmap[(x, y)]['r'] = dmap[(x, y + 1)]['r']  
                else:
                    dmap[(x, y)]['r'] = (x, y)
        
        bmap = {ball : (0, '', ball)}
        distance = lambda pa, pb: abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
        visited = set()
        while bmap:
            dist, path, p  = min(bmap.values())
            if p == hole:
                return path
            del bmap[p]
            visited.add(p)
            for dir in 'dlru':
                if dir not in dmap[p]: continue
                np = dmap[p][dir]
                ndist = dist + distance(p, np)
                npath = path + dir
                if np not in visited and (np not in bmap or (ndist, npath, np) < bmap[np]):
                    bmap[np] = (ndist, npath, np)
        return 'impossible'
                
