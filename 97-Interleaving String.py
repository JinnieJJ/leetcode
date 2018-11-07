class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if (i, j, k) not in memory:
                memory[(i, j, k)] = (k >= l3) or \
                (i < l1 and s3[k] == s1[i] and dfs(i+1, j, k+1)) or \
                (j < l2 and s3[k] == s2[j] and dfs(i, j+1, k+1))
            return memory[(i, j, k)]
        l1, l2, l3, memory = len(s1), len(s2), len(s3), {}
        if l3 != l1 + l2: 
            return False
        return dfs(0, 0, 0)
                
