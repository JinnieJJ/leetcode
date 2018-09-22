class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        similar = collections.defaultdict(set)
        for w1, w2 in pairs:
            similar[w1].add(w2)
            similar[w2].add(w1)
        
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and w2 not in similar[w1]:
                return False
        return True
