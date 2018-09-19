# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
              
        adj = [[0 for _ in range(len(wordlist))] for _ in range(len(wordlist))]
        for i in range(len(wordlist)):
            adj[i][i] = 6
            for j in range(0, i):
                score = sum([wordlist[i][c] == wordlist[j][c] for c in range(6)])
                adj[i][j] = adj[j][i] = score
        
        d = collections.defaultdict(dict)
        for i in range(len(wordlist)):
            for j in range(i+1):
                if adj[i][j] not in d[wordlist[i]]: 
                    d[wordlist[i]][adj[i][j]] = []
                if adj[i][j] not in d[wordlist[j]]: 
                    d[wordlist[j]][adj[i][j]] = []
                d[wordlist[i]][adj[i][j]].append(wordlist[j])
                d[wordlist[j]][adj[i][j]].append(wordlist[i])
        
        score = master.guess(wordlist[0])
        if score == 6:
            return
        s = set(d[wordlist[0]][score])
        cnt = 1
        while cnt < 10:
            word = list(s)[0]
            score = master.guess(word)
            if score == 6: 
                return
            s = s & set(d[word][score])  # 交集
            cnt += 1
