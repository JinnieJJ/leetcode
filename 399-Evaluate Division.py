# class Solution:
#     def calcEquation(self, equations, values, queries):
#         """
#         :type equations: List[List[str]]
#         :type values: List[float]
#         :type queries: List[List[str]]
#         :rtype: List[float]
#         """
#         g = collections.defaultdict(lambda:collections.defaultdict(int))
#         for (s, t), v in zip(equations, values):
#             g[s][t] = v
#             g[t][s] = 1.0 / v
#         for k in g:
#             g[k][k] = 1.0
#             for s in g:
#                 for t in g:
#                     if g[s][k] and g[k][t]:
#                         g[s][t] = g[s][k] * g[k][t]
#         ans = []
#         for s, t in queries:
#             ans.append(g[s][t] if g[s][t] else -1.0)
#         return ans

from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations or not values or not queries:
            return []
        graph = self.build_graph(equations, values)
        res = []
        for root, target in queries:
            if root not in graph or target not in graph:
                res.append(-1.0)
            else:
                res.append(self.evaluate(graph, root, target, 1.0, set()))
        return res


    def build_graph(self, equations, values):
        graph = defaultdict(list)
        for i, (e1, e2) in enumerate(equations):
            graph[e1].append((e2, values[i]))
            if values[i] != 0:
                graph[e2].append((e1, 1.0 / values[i]))
        return graph

    def evaluate(self, graph, root, target, current_val, visited):
        if root == target:
            return current_val
        for key, value in graph[root]:
            if key in visited:
                continue
            visited.add(key)
            return_value = self.evaluate(graph, key, target, current_val*value, visited)
            if return_value != -1:
                return return_value
        return -1

    
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class UnionFind(object):
    def __init__(self, equations):
        self.parents = {}
        for e1, e2 in equations:
            self.parents[e1] = (e1, 1.0)
            self.parents[e2] = (e2, 1.0)
    
    def find(self, var):
        if var not in self.parents:
            return (None, None)
        if var == self.parents[var][0]:
            return self.parents[var]
        parent = self.find(self.parents[var][0])
        self.parents[var] = (parent[0], self.parents[var][1] * parent[1])
        return self.parents[var]
    
    def union(self, var1, var2, val):
        parent1 = self.find(var1)
        parent2 = self.find(var2)
        if parent1[0] != parent2[0]:
            self.parents[parent1[0]] = (parent2[0], parent2[1] * val/parent1[1])

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        u = UnionFind(equations)
        for var, val in zip(equations, values):
            u.union(var[0], var[1], val)
        res = []
        for q1, q2 in queries:
            parent1 = u.find(q1)
            parent2 = u.find(q2)
            if not parent1[0] or not parent2[0] or parent1[0] != parent2[0]:
                res.append(-1.0)
            else:
                res.append(parent1[1] / parent2[1])
        return res
