class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            dict = {}
            for  x, y in zip(pattern, word):
                if dict.setdefault(x, y) != y:
                    return False
            return len(set(dict.values())) == len(dict.values())
        
        return list(filter(match, words))
