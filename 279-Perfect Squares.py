class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i*i <= n:
            lst.append(i*i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            tmp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    tmp.add(x-y)
            toCheck = tmp
        return cnt
