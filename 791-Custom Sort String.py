class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counterT = collections.Counter(T)
        ans = ''
        for c in S:
            ans += c * counterT[c]
            del counterT[c]
        return ans + ''.join(k * v for k, v in counterT.items())
