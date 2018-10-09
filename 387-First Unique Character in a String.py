class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        candidates = set()
        
        for i, c in enumerate(s):
            if c in lookup:
                candidates.discard(lookup[c])
            else:
                lookup[c] = i
                candidates.add(i)
        return min(candidates) if candidates else -1
