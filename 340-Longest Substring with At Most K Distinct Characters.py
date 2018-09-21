class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest = 0
        start = 0
        distinct_count = 0
        visited = [0 for _ in range(256)]

        for i, c in enumerate(s):
            if visited[ord(c)] == 0:
                distinct_count += 1
            visited[ord(c)] += 1

            while distinct_count > k:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1

            longest = max(longest, i-start+1)
        return longest
