class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        offset = 0
        for i, s, t in sorted(zip(indexes, sources, targets)):
            l = len(s)
            if S[i+offset:i+l+offset] == s:
                S = S[:i+offset] + t + S[i+l+offset:] 
                offset += len(t) - l
        return S  
