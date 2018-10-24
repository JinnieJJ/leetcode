class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not self.dict[len(word)]:
            return False
        for w in self.dict[len(word)]:
            diff = 0
            for a, b in zip(w, word):
                diff += a != b
            if diff == 1:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
