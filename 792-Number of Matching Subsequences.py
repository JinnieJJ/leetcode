class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        dict = collections.defaultdict(list)
        
        for word in words:
            dict[word[0]].append(word)
        
        for s in S:
            queue = dict[s]
            for i in range(len(queue)):
                word = queue.pop(0)
                if len(word) == 1:
                    res += 1
                    continue
                word = word[1:]
                dict[word[0]].append(word)
        return res
