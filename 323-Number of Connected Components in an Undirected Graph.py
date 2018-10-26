class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = {}
        for e in edges:
            if e[0] not in dic:
                dic[e[0]] = [e[1]]
            else:
                dic[e[0]].append(e[1])
            if e[1] not in dic:
                dic[e[1]] = [e[0]]
            else:
                dic[e[1]].append(e[0])
        seen = [0] * n
        count = 0
        for i in range(n):
            if seen[i] == 0:
                count += 1
                stack = [i]
                while stack:
                    u = stack.pop()
                    seen[u] = 1
                    if u in dic:
                        for neighbor in dic[u]:
                            if seen[neighbor] == 0:
                                stack.append(neighbor)
        return count
