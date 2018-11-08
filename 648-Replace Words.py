class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        class Trie:  
            def __init__(self):
                self.next = {}
                self.end = False
                
            def insert(self, word):
                cur = self
                for c in word:
                    if c in cur.next:
                        cur = cur.next[c]
                    else:
                        cur.next[c] = Trie()
                        cur = cur.next[c]
                cur.end = True
        
        trie = Trie()
        for word in dict:
            trie.insert(word)
        sentence = sentence.split()
        ans = []
        
        for word in sentence:
            pref = ""
            cur = trie
            for i, c in enumerate(word):
                if c not in cur.next:
                    ans.append(word)
                    break
                cur = cur.next[c]
                pref = pref + c
                if cur.end or i == len(word) - 1:
                    ans.append(pref)
                    break
        return " ".join(ans)
        
        
