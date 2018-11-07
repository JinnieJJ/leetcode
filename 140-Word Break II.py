class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        l = len(s)
        wordDict = set(wordDict)
        memo = {}
        def search(i):
            if i in memo:
                return memo[i]
            if i == l:
                return ['']
            record = []
            for j in range(i,l):
                if s[i:j+1] in wordDict:
                    for word in search(j+1):
                        if word != '':
                            record.append(s[i:j+1] + ' ' + word)
                        else:
                            record.append(s[i:j+1])
            memo[i] = record
            return record
        return search(0)
