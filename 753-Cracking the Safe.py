class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        ans = "0" * (n - 1)
        visited = set()
        for x in range(k ** n):
            if  n == 1:
                current = ""
            else:
                current = ans[-(n-1):]
            for y in range(k-1, -1, -1):
                if current + str(y) not in visited:
                    visited.add(current + str(y))
                    ans += str(y)
                    break
        return ans
