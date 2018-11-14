class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring_length = 0
        current_length = 0
        dic = {}
        for index, char in enumerate(s):
            if char not in dic:
                current_length += 1
            else:
                current_length = min(index-dic[char], current_length + 1)
            dic[char] = index
            substring_length = max(substring_length, current_length)
        return substring_length
        
        
