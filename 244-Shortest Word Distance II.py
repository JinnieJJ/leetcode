class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordIndex = collections.defaultdict(list)
        for i in range(len(words)):
            self.wordIndex[words[i]].append(i)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indexes1 = self.wordIndex[word1]
        indexes2 = self.wordIndex[word2]
        i, j, dist = 0, 0, float("inf")
        while i < len(indexes1) and j < len(indexes2):
            dist = min(dist, abs(indexes1[i] - indexes2[j]))
            if indexes1[i] < indexes2[j]:
                i += 1
            else:
                j += 1
        return dist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
