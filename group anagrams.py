class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        result = []
        for s in strs:
            sorted_s = ("").join(sorted(s))
            if sorted_s not in dict:
                dict[sorted_s] = [s]
            else:
                dict[sorted_s].append(s)
        for str in dict.values():
            str.sort()
            result.append(str)
        return result
