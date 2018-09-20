class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0

class AutocompleteSystem:
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])
            
    def addRecord(self, sentence, hot):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        p.rank -= hot
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        results = []
        if c != '#':
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results)[:3]]
    
    def search(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)
        
    def dfs(self, root):
        ret = []
        if root:
            if root.isEnd:
                ret.append((root.rank, root.data))
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
