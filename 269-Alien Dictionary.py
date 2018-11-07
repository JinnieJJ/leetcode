from collections import deque

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.visited = {}
        self.graph = {}
        self.results = deque()
        characters = set()
        
        for word in words:
            for char in word:
                self.visited[char] = 0
                self.graph[char] = []
                characters.add(char)
                
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            success = self.addEdge(word1, word2)
            if not success:
                return ""
        
        for char in characters:
            success = self.topologicalSort(char)
            if not success:
                return ""
            
        return "".join(list(self.results))
            
    def topologicalSort(self, char):
        if self.visited[char] == -1: # detected cycle
            return False
        if self.visited[char] == 1: #char has been visited and completed topological sort on
            return True
        
        self.visited[char] = -1
        
        for neigh in self.graph[char]:
            success = self.topologicalSort(neigh)
            if not success:
                return False
        
        self.visited[char] = 1
        self.results.appendleft(char)
        return True
    
    def _addEdge(self, var1, var2):
        self.graph[var1].append(var2)
        
    def addEdge(self, word1, word2):
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                self._addEdge(char1, char2)
                return True
        
        if len(word1) > len(word2):
            return False
        return True
