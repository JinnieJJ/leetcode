class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return False
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                stack = [(i, 0)]
                while stack:
                    point, value = stack.pop()
                    for neigh in graph[point]:
                        if neigh in color:
                            if color[neigh] != (value+1) % 2:
                                return False
                        else:
                            stack.append((neigh, (value+1) % 2))
                            color[neigh] = (value+1) % 2
        return True
