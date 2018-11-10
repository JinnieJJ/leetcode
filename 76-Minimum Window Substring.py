class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        miss = len(t)
        i = 0 # sliding window is s[i:j]
        I = J = 0 # final indexes for the result
        for j, c in enumerate(s, 1):
            # j start from 1
            miss -= (need[c] > 0)
            need[c] -= 1
            if not miss:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I: J]
