class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        str_list  = S.split('-')
        s = ''.join(str_list)
        
        result = ""
        while s:
            result = "-"+s[-K:]+result
            s = s[:-K]
        return result[1:].upper()
