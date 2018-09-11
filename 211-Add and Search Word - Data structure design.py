class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordDict = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) in self.wordDict:
            self.wordDict[len(word)].add(word)
        else:
            self.wordDict[len(word)] = set([word])
    
    def filter(self, wordPool, i, c):
        if c == '.':
            return wordPool
        return [word for word in wordPool if word[i] == c or word[i] == '.']

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.wordDict:
            return False
        if word in self.wordDict[len(word)]:
            return True
        wordPool = list(self.wordDict[len(word)])
        for i, c in enumerate(word):
            wordPool = self.filter(wordPool, i, c)
            if wordPool == []:
                return False
        return True
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
