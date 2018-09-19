class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        sa, sb = len(A), len(B)
        x = 1
        if sb <= sa:
            while x <= 2:
                if B in A * x:
                    return x
                x += 1
            return -1
        
        while (x-1) * sa <= sb + sa:
            if B in A * x: 
                return x
            x += 1
        return -1
