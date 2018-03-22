class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i+1>len(string) or strs[0][i] != string[i]:
                    return strs[0][:i]
        
        return strs[0]
                
