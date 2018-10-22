class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefixes = collections.defaultdict(set)
        self.suffixes = collections.defaultdict(set)
        self.weights = {}
        
        for i, word in enumerate(words):
            prefix, suffix = '', ''
            for char in [''] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [''] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = i
        

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        weight = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
