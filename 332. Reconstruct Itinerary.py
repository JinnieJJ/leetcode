from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)
        for t in tickets:
            self.graph[t[0]].append(t[1])
        self.visited = {}
        for start, dests in self.graph.items():
            dests.sort()
            self.visited[start] = [False] * len(dests)
        self.length = len(tickets) + 1
        return self.dfs("JFK", ["JFK"])
        
    def dfs(self, start, route):
        if len(route) == self.length:
            return route
        
        for i, dest in enumerate(self.graph[start]):
            if not self.visited[start][i]:
                self.visited[start][i] = True
                nextRoute = self.dfs(dest, route + [dest])
                self.visited[start][i] = False
                if nextRoute:
                    return nextRoute
        return None
