from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        neighbors = defaultdict(list)
        for word in wordList:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                neighbors[token].append(word)
        
        while queue:       
            word, length = queue.popleft()
            if sum([word[x] != endWord[x] for x in range(len(endWord))]) <= 1:
                return length + 1
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                if token in neighbors:
                    for next_word in neighbors[token]:
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append((next_word, length + 1))
        return 0
